from database.db_manager import Database

class TrendModel:
    """Model para gerenciar dados de tendências"""
    
    def __init__(self):
        self.db = Database()
    
    def save_trend(self, term, platform, search_volume, region=None):
        """Salva uma tendência"""
        return self.db.save_trend(term, platform, search_volume, region)
    
    def get_trends_by_platform(self, platform, limit=50):
        """Busca tendências por plataforma"""
        return self.db.get_trends(platform=platform, limit=limit)
    
    def get_all_trends(self, limit=100):
        """Busca todas as tendências"""
        return self.db.get_trends(limit=limit)
    
    def save_user_search(self, search_term):
        """Salva pesquisa do usuário"""
        return self.db.save_user_search(search_term)
    
    def format_trends_for_display(self, trends):
        """Formata tendências para exibição"""
        formatted = []
        for trend in trends:
            formatted.append({
                'term': trend[0],
                'platform': trend[1],
                'search_volume': trend[2],
                'region': trend[3] or 'Brasil',
                'date': trend[4]
            })
        return formatted