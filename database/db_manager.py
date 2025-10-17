import sqlite3
import os
from datetime import datetime

class Database:
    """Classe para gerenciar o banco de dados"""
    
    def __init__(self, db_path="database/trends.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Retorna uma conexão com o banco"""
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        """Inicializa o banco de dados com as tabelas necessárias"""
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tabela de tendências
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trends (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                term TEXT NOT NULL,
                platform TEXT NOT NULL,
                search_volume INTEGER,
                region TEXT,
                date_collected DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de pesquisas do usuário
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_searches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                search_term TEXT NOT NULL,
                search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_trend(self, term, platform, search_volume, region=None):
        """Salva uma tendência no banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO trends (term, platform, search_volume, region, date_collected)
            VALUES (?, ?, ?, ?, DATE('now'))
        ''', (term, platform, search_volume, region))
        
        conn.commit()
        conn.close()
    
    def get_trends(self, platform=None, limit=50):
        """Busca tendências do banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = '''
            SELECT term, platform, search_volume, region, date_collected
            FROM trends
            WHERE date_collected >= DATE('now', '-3 days')
        '''
        
        params = []
        if platform:
            query += ' AND platform = ?'
            params.append(platform)
            
        query += ' ORDER BY search_volume DESC LIMIT ?'
        params.append(limit)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        
        return results
    
    def save_user_search(self, search_term):
        """Salva pesquisa do usuário"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO user_searches (search_term)
            VALUES (?)
        ''', (search_term,))
        
        conn.commit()
        conn.close()