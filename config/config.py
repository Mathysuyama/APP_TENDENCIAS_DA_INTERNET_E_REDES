import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class Config:
    """Configurações da aplicação"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # APIs das Redes Sociais
    FACEBOOK_ACCESS_TOKEN = os.environ.get('FACEBOOK_ACCESS_TOKEN')
    INSTAGRAM_ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')
    TIKTOK_API_KEY = os.environ.get('TIKTOK_API_KEY')
    
    # Configurações do Banco
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///database/trends.db'
    
    # Configurações Gerais
    DEFAULT_SEARCH_DAYS = int(os.environ.get('DEFAULT_SEARCH_DAYS', 3))
    MAX_RESULTS_PER_PLATFORM = int(os.environ.get('MAX_RESULTS_PER_PLATFORM', 50))