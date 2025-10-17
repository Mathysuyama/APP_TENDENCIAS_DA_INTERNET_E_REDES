# Sistema de Análise de Tendências para Marketing de Afiliados

Um sistema Python MVC completo para análise de tendências de pesquisa em Google e redes sociais, otimizado para estratégias de marketing de afiliados no Mercado Livre.

## 🎯 Funcionalidades

### ✅ Implementadas
- **Busca de Tendências**: Pesquisa termos trending no Google, Facebook, Instagram e TikTok
- **Ranking Dinâmico**: Exibe palavras-chave ordenadas por volume de pesquisa
- **Análise Regional**: Mostra distribuição de interesse por estados/regiões
- **Interface Web**: Dashboard completo para consultas e visualização
- **Filtros por Plataforma**: Análise específica por rede social
- **Banco de Dados**: Armazenamento local SQLite para histórico

### 🚀 Como Usar

1. **Pesquisa Específica**: Digite um termo na caixa de busca
2. **Tendências Atuais**: Deixe em branco para ver termos em alta dos últimos 3 dias
3. **Ranking Completo**: Visualize todos os dados coletados organizados
4. **Filtros**: Analise por plataforma específica (Google, Facebook, Instagram, TikTok)

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8+
- pip

### Configuração

1. **Clone o repositório**:
```bash
git clone <seu-repositorio>
cd APP_TENDENCIAS_DA_INTERNET_E_REDES
```

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

3. **Configure variáveis de ambiente**:
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais de API
```

4. **Execute a aplicação**:
```bash
python run.py
```

5. **Acesse no navegador**:
```
http://localhost:5000
```

## 📁 Estrutura do Projeto

```
APP_TENDENCIAS_DA_INTERNET_E_REDES/
├── app/
│   ├── controllers/          # Controladores (Rotas e lógica)
│   ├── models/              # Modelos (Dados e serviços)
│   ├── templates/           # Templates HTML
│   ├── static/              # Arquivos estáticos (CSS, JS)
│   └── __init__.py
├── config/                  # Configurações da aplicação
├── database/               # Gerenciamento do banco de dados
├── .github/               # Documentação do projeto
├── requirements.txt       # Dependências Python
├── .env.example          # Exemplo de variáveis de ambiente
└── run.py               # Arquivo principal para executar
```

## 🔧 APIs Utilizadas

### Google Trends
- **Biblioteca**: `pytrends`
- **Funcionalidade**: Busca termos trending e volume de pesquisa
- **Cobertura**: Brasil e regiões

### Redes Sociais
- **Facebook**: Facebook Graph API (requer token)
- **Instagram**: Instagram API (requer token)
- **TikTok**: TikTok API (requer chave)

> **Nota**: As APIs das redes sociais estão simuladas no momento. Para implementação completa, configure as credenciais no arquivo `.env`.

## 📊 Funcionalidades por Tela

### 1. Dashboard Principal (`/`)
- Visão geral do sistema
- Acesso rápido às funcionalidades
- Cards por plataforma

### 2. Pesquisa (`/search`)
- Caixa de busca para termos específicos
- Exemplos de pesquisas populares
- Dicas de otimização

### 3. Resultados (`/search` - POST)
- Exibição de dados por plataforma
- Volume de pesquisa e regiões
- Análise comparativa

### 4. Ranking (`/ranking`)
- Lista completa ordenada por volume
- Filtros por plataforma
- Estatísticas consolidadas

## 🎨 Interface

- **Framework**: Bootstrap 5
- **Ícones**: Font Awesome 6
- **Design**: Responsivo e moderno
- **Cores**: Diferenciadas por plataforma

## 📈 Dados Coletados

Para cada termo analisado:
- **Termo**: Palavra-chave pesquisada
- **Plataforma**: Google, Facebook, Instagram, TikTok
- **Volume**: Número de pesquisas/interesse
- **Região**: Estados/regiões com maior interesse
- **Data**: Quando o dado foi coletado

## 🚀 Próximas Melhorias

- [ ] Integração real com APIs das redes sociais
- [ ] Sistema de alertas para termos específicos
- [ ] Exportação de dados (CSV, Excel)
- [ ] Gráficos e visualizações avançadas
- [ ] Agendamento automático de coletas
- [ ] Sistema de usuários e favoritos
- [ ] Integração com APIs do Mercado Livre
- [ ] Análise de concorrência
- [ ] Sugestões automáticas de produtos

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

- **Issues**: Reporte bugs ou solicite features
- **Wiki**: Documentação detalhada
- **Discussions**: Dúvidas e discussões gerais

---

**Desenvolvido para otimizar suas estratégias de marketing de afiliados** 🎯