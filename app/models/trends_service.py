from pytrends.request import TrendReq
import requests
import json
from datetime import datetime, timedelta

class GoogleTrendsService:
    """Serviço para buscar tendências do Google"""
    
    def __init__(self):
        self.pytrends = TrendReq(hl='pt-BR', tz=180)
    
    def get_trending_searches(self, country='BR'):
        """Busca termos em alta no Google"""
        try:
            trending = self.pytrends.trending_searches(pn=country)
            return trending[0].tolist()[:20]  # Top 20
        except Exception as e:
            print(f"Erro ao buscar Google Trends: {e}")
            return []
    
    def get_keyword_data(self, keyword, region='BR'):
        """Busca dados específicos de uma palavra-chave"""
        try:
            self.pytrends.build_payload([keyword], timeframe='now 7-d', geo=region)
            interest_over_time = self.pytrends.interest_over_time()
            
            if not interest_over_time.empty:
                # Média do interesse nos últimos 7 dias
                avg_interest = interest_over_time[keyword].mean()
                return int(avg_interest)
            return 0
        except Exception as e:
            print(f"Erro ao buscar dados da palavra-chave {keyword}: {e}")
            return 0
    
    def get_regional_interest(self, keyword):
        """Busca interesse por região"""
        try:
            self.pytrends.build_payload([keyword], timeframe='now 7-d', geo='BR')
            regional = self.pytrends.interest_by_region(resolution='REGION')
            
            if not regional.empty:
                # Retorna top 5 estados brasileiros
                top_regions = regional.sort_values(by=keyword, ascending=False).head(5)
                return top_regions.to_dict()[keyword]
            else:
                # Fallback com estados brasileiros simulados baseados em população
                return self._get_simulated_brazilian_regions(keyword)
        except Exception as e:
            print(f"Erro ao buscar dados regionais: {e}")
            return self._get_simulated_brazilian_regions(keyword)
    
    def _get_simulated_brazilian_regions(self, keyword):
        """Simula dados regionais para estados brasileiros"""
        import random
        
        # Estados brasileiros com pesos baseados em população/economia
        estados_brasil = {
            'São Paulo': random.randint(80, 100),
            'Rio de Janeiro': random.randint(60, 85),
            'Minas Gerais': random.randint(55, 80),
            'Rio Grande do Sul': random.randint(45, 70),
            'Paraná': random.randint(40, 65),
            'Bahia': random.randint(35, 60),
            'Santa Catarina': random.randint(35, 55),
            'Goiás': random.randint(30, 50),
            'Pernambuco': random.randint(25, 45),
            'Ceará': random.randint(20, 40),
            'Pará': random.randint(18, 35),
            'Maranhão': random.randint(15, 30),
            'Paraíba': random.randint(12, 25),
            'Mato Grosso': random.randint(15, 30),
            'Distrito Federal': random.randint(40, 60),
            'Alagoas': random.randint(10, 20),
            'Piauí': random.randint(8, 18),
            'Rio Grande do Norte': random.randint(12, 22),
            'Sergipe': random.randint(8, 16),
            'Espírito Santo': random.randint(25, 40),
            'Mato Grosso do Sul': random.randint(15, 28),
            'Rondônia': random.randint(10, 20),
            'Acre': random.randint(5, 12),
            'Amazonas': random.randint(12, 25),
            'Roraima': random.randint(3, 8),
            'Amapá': random.randint(3, 8),
            'Tocantins': random.randint(8, 15)
        }
        
        # Retorna os top 5 estados ordenados
        sorted_estados = sorted(estados_brasil.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_estados[:5])

class SocialMediaService:
    """Serviço para buscar dados das redes sociais"""
    
    def __init__(self, facebook_token=None, instagram_token=None, tiktok_key=None):
        self.facebook_token = facebook_token
        self.instagram_token = instagram_token
        self.tiktok_key = tiktok_key
    
    def get_facebook_trends(self):
        """Simula busca de tendências do Facebook"""
        # Nota: API real do Facebook requer aprovação e tokens específicos
        # Por enquanto, retornamos dados simulados
        mock_trends = [
            "Black Friday", "Natal", "Cyber Monday", "iPhone 15",
            "WhatsApp", "Instagram", "TikTok", "YouTube",
            "Amazon", "Mercado Livre", "Shopee", "Magazine Luiza"
        ]
        return mock_trends[:10]
    
    def get_instagram_trends(self):
        """Simula busca de tendências do Instagram"""
        mock_trends = [
            "#blackfriday", "#natal2024", "#moda", "#beleza",
            "#tecnologia", "#casa", "#decoracao", "#fitness",
            "#food", "#viagem", "#mercadolivre", "#afiliados"
        ]
        return mock_trends[:10]
    
    def get_tiktok_trends(self):
        """Simula busca de tendências do TikTok"""
        mock_trends = [
            "viral dance", "receitas rapidas", "dicas de casa",
            "maquiagem", "produtos baratos", "gadgets",
            "decoracao", "organizacao", "DIY", "unboxing"
        ]
        return mock_trends[:10]
    
    def get_youtube_trends(self):
        """Simula busca de tendências do YouTube"""
        mock_trends = [
            "review iPhone 15", "unboxing produtos", "como usar Air Fryer",
            "teste de produtos", "melhores gadgets", "review notebook",
            "produtos baratos", "ofertas imperdíveis", "Black Friday",
            "dicas de compras", "analise produtos", "tutorial tecnologia"
        ]
        return mock_trends[:10]
    
    def search_term_volume(self, term, platform):
        """Simula volume de busca para um termo específico"""
        import random
        # Simula volume baseado na plataforma
        base_volume = {
            'facebook': random.randint(1000, 50000),
            'instagram': random.randint(500, 30000),
            'tiktok': random.randint(2000, 100000),
            'youtube': random.randint(3000, 80000)  # YouTube tem alto volume!
        }
        return base_volume.get(platform.lower(), random.randint(100, 10000))
    
    def get_brazilian_regions_for_social(self, term, platform):
        """Simula dados regionais para redes sociais com estados brasileiros"""
        import random
        
        # Estados com diferentes pesos baseados na plataforma
        if platform.lower() == 'facebook':
            # Facebook mais popular em estados maiores
            estados = {
                'São Paulo': random.randint(15000, 25000),
                'Rio de Janeiro': random.randint(12000, 20000),
                'Minas Gerais': random.randint(10000, 18000),
                'Bahia': random.randint(8000, 15000),
                'Rio Grande do Sul': random.randint(7000, 14000)
            }
        elif platform.lower() == 'instagram':
            # Instagram mais popular em estados jovens/urbanos
            estados = {
                'São Paulo': random.randint(8000, 15000),
                'Rio de Janeiro': random.randint(7000, 13000),
                'Distrito Federal': random.randint(5000, 10000),
                'Santa Catarina': random.randint(4000, 8000),
                'Espírito Santo': random.randint(3000, 6000)
            }
        elif platform.lower() == 'tiktok':
            # TikTok mais popular entre jovens
            estados = {
                'São Paulo': random.randint(20000, 35000),
                'Rio de Janeiro': random.randint(15000, 28000),
                'Minas Gerais': random.randint(12000, 22000),
                'Paraná': random.randint(8000, 15000),
                'Ceará': random.randint(6000, 12000)
            }
        else:  # YouTube
            # YouTube popular em todas as idades, especialmente para reviews
            estados = {
                'São Paulo': random.randint(25000, 40000),
                'Rio de Janeiro': random.randint(18000, 32000),
                'Minas Gerais': random.randint(15000, 25000),
                'Rio Grande do Sul': random.randint(12000, 20000),
                'Paraná': random.randint(10000, 18000)
            }
        
        return estados

class TrendsAggregator:
    """Agregador de todas as fontes de tendências"""
    
    def __init__(self, facebook_token=None, instagram_token=None, tiktok_key=None):
        self.google_service = GoogleTrendsService()
        self.social_service = SocialMediaService(facebook_token, instagram_token, tiktok_key)
    
    def get_all_trends(self):
        """Busca tendências de todas as plataformas"""
        all_trends = []
        
        # Google Trends
        google_trends = self.google_service.get_trending_searches()
        for term in google_trends:
            volume = self.google_service.get_keyword_data(term)
            all_trends.append({
                'term': term,
                'platform': 'Google',
                'volume': volume,
                'regions': self.google_service.get_regional_interest(term)
            })
        
        # Facebook
        facebook_trends = self.social_service.get_facebook_trends()
        for term in facebook_trends:
            volume = self.social_service.search_term_volume(term, 'facebook')
            regions = self.social_service.get_brazilian_regions_for_social(term, 'facebook')
            all_trends.append({
                'term': term,
                'platform': 'Facebook',
                'volume': volume,
                'regions': regions
            })
        
        # Instagram
        instagram_trends = self.social_service.get_instagram_trends()
        for term in instagram_trends:
            volume = self.social_service.search_term_volume(term, 'instagram')
            regions = self.social_service.get_brazilian_regions_for_social(term, 'instagram')
            all_trends.append({
                'term': term,
                'platform': 'Instagram',
                'volume': volume,
                'regions': regions
            })
        
        # TikTok
        tiktok_trends = self.social_service.get_tiktok_trends()
        for term in tiktok_trends:
            volume = self.social_service.search_term_volume(term, 'tiktok')
            regions = self.social_service.get_brazilian_regions_for_social(term, 'tiktok')
            all_trends.append({
                'term': term,
                'platform': 'TikTok',
                'volume': volume,
                'regions': regions
            })
        
        # YouTube
        youtube_trends = self.social_service.get_youtube_trends()
        for term in youtube_trends:
            volume = self.social_service.search_term_volume(term, 'youtube')
            regions = self.social_service.get_brazilian_regions_for_social(term, 'youtube')
            all_trends.append({
                'term': term,
                'platform': 'YouTube',
                'volume': volume,
                'regions': regions
            })
        
        # Ordenar por volume
        all_trends.sort(key=lambda x: x['volume'], reverse=True)
        return all_trends
    
    def search_specific_term(self, term):
        """Busca dados específicos de um termo"""
        results = []
        
        # Google
        google_volume = self.google_service.get_keyword_data(term)
        google_regions = self.google_service.get_regional_interest(term)
        results.append({
            'term': term,
            'platform': 'Google',
            'volume': google_volume,
            'regions': google_regions
        })
        
        # Redes sociais (volumes simulados)
        for platform in ['Facebook', 'Instagram', 'TikTok', 'YouTube']:
            volume = self.social_service.search_term_volume(term, platform.lower())
            regions = self.social_service.get_brazilian_regions_for_social(term, platform.lower())
            results.append({
                'term': term,
                'platform': platform,
                'volume': volume,
                'regions': regions
            })
        
        return results