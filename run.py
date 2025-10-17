from app import create_app
from database.db_manager import Database

app = create_app()

if __name__ == '__main__':
    # Inicializar banco de dados
    db = Database()
    
    # Executar aplicação
    app.run(debug=True, host='0.0.0.0', port=5000)