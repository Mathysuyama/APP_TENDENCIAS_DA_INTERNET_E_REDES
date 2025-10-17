from flask import Blueprint, render_template, request, jsonify, flash
from app.models.trend_model import TrendModel
from app.models.trends_service import TrendsAggregator

# Criar blueprint
trends_bp = Blueprint('trends', __name__)

# Inicializar serviços
trend_model = TrendModel()
trends_aggregator = TrendsAggregator()

@trends_bp.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@trends_bp.route('/search', methods=['GET', 'POST'])
def search_trends():
    """Buscar tendências"""
    if request.method == 'POST':
        search_term = request.form.get('search_term', '').strip()
        
        if search_term:
            # Buscar termo específico
            trend_model.save_user_search(search_term)
            results = trends_aggregator.search_specific_term(search_term)
            
            # Salvar resultados no banco
            for result in results:
                for region, volume in result['regions'].items():
                    trend_model.save_trend(
                        result['term'], 
                        result['platform'], 
                        volume, 
                        region
                    )
            
            # Converter regions para lista para evitar problemas de template
            for result in results:
                if isinstance(result['regions'], dict):
                    result['regions'] = list(result['regions'].items())
            
            return render_template('search_results.html', 
                                 results=results, 
                                 search_term=search_term)
        else:
            # Buscar tendências gerais dos últimos 3 dias
            hot_trends = trends_aggregator.get_all_trends()
            
            # Salvar no banco
            for trend in hot_trends[:50]:  # Limitar a 50 primeiros
                for region, volume in trend['regions'].items():
                    trend_model.save_trend(
                        trend['term'], 
                        trend['platform'], 
                        volume, 
                        region
                    )
            
            # Converter regions para lista para evitar problemas de template
            for trend in hot_trends:
                if isinstance(trend['regions'], dict):
                    trend['regions'] = list(trend['regions'].items())
            
            return render_template('trending.html', trends=hot_trends)
    
    return render_template('search.html')

@trends_bp.route('/ranking')
def ranking():
    """Exibir ranking de tendências"""
    all_trends = trend_model.get_all_trends(limit=100)
    formatted_trends = trend_model.format_trends_for_display(all_trends)
    
    return render_template('ranking.html', trends=formatted_trends)

@trends_bp.route('/api/trends')
def api_trends():
    """API para buscar tendências"""
    platform = request.args.get('platform')
    limit = int(request.args.get('limit', 50))
    
    if platform:
        trends = trend_model.get_trends_by_platform(platform, limit)
    else:
        trends = trend_model.get_all_trends(limit)
    
    formatted_trends = trend_model.format_trends_for_display(trends)
    return jsonify(formatted_trends)

@trends_bp.route('/api/search/<term>')
def api_search(term):
    """API para buscar termo específico"""
    results = trends_aggregator.search_specific_term(term)
    return jsonify(results)

@trends_bp.route('/regional/<term>')
def regional_analysis(term):
    """Análise regional detalhada de um termo"""
    results = trends_aggregator.search_specific_term(term)
    
    # Converter regions para lista para template
    for result in results:
        if isinstance(result['regions'], dict):
            result['regions'] = list(result['regions'].items())
    
    # Organizar dados por estado
    regional_data = {}
    for result in results:
        for region, volume in result['regions']:
            if region not in regional_data:
                regional_data[region] = {}
            regional_data[region][result['platform']] = volume
    
    return render_template('regional_analysis.html', 
                         term=term, 
                         results=results,
                         regional_data=regional_data)

@trends_bp.route('/refresh')
def refresh_trends():
    """Atualizar tendências"""
    try:
        hot_trends = trends_aggregator.get_all_trends()
        
        # Salvar no banco
        for trend in hot_trends:
            for region, volume in trend['regions'].items():
                trend_model.save_trend(
                    trend['term'], 
                    trend['platform'], 
                    volume, 
                    region
                )
        
        flash(f'Tendências atualizadas! {len(hot_trends)} termos coletados.', 'success')
    except Exception as e:
        flash(f'Erro ao atualizar tendências: {str(e)}', 'error')
    
    return render_template('index.html')