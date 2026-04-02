import json
import os

# Caminho do arquivo para facilitar mudanças futuras
ARQUIVO_DB = "empresas.json"

def carregar_empresas():
    """Carrega os dados do arquivo JSON ou cria dados iniciais se não existir."""
    if os.path.exists(ARQUIVO_DB):
        try:
            with open(ARQUIVO_DB, "r", encoding="utf-8") as f:
                empresas = json.load(f)
        except (json.JSONDecodeError, Exception):
            # Se o arquivo estiver corrompido, inicia vazio para não travar o app
            empresas = {}
    else:
        empresas = {}

    # Dados Iniciais (Seed Data) - Caso o banco esteja vazio
    # Aqui coloquei nomes "Premium" como você queria para o seu portfólio
    if not empresas:
        empresas = {
            "Veloce Bistro": {
                "senha": "admin", 
                "categoria": "Italiana", 
                "descricao": "Massas artesanais e pizzas no forno a lenha.",
                "produtos": {"Pizza Margherita": 45.90, "Lasanha Bolonhesa": 38.00}, 
                "publicada": True,
                "horario": {"abertura": "18:00", "fechamento": "23:30"}, 
                "logo": "🍕"
            },
            "Zenith Sushi": {
                "senha": "admin", 
                "categoria": "Japonesa", 
                "descricao": "O melhor da culinária oriental contemporânea.",
                "produtos": {"Combo 20 peças": 55.00, "Temaki Salmão": 22.50}, 
                "publicada": True,
                "horario": {"abertura": "11:00", "fechamento": "22:00"}, 
                "logo": "🍣"
            }
        }
        salvar_empresas(empresas) # Salva logo de cara para criar o arquivo
    
    # Validação de integridade: Garante que todas as empresas tenham todos os campos necessários
    for nome, dados in empresas.items():
        if not isinstance(dados, dict): continue # Pula se não for um dicionário
        
        campos_obrigatorios = {
            "senha": "123",
            "categoria": "Geral",
            "descricao": "",
            "produtos": {},
            "publicada": False,
            "horario": {"abertura": "00:00", "fechamento": "23:59"},
            "logo": "🏪"
        }
        
        # Preenche campos faltantes se o usuário cadastrou de forma incompleta antigamente
        for campo, valor_padrao in campos_obrigatorios.items():
            if campo not in dados:
                dados[campo] = valor_padrao
                
    return empresas

def salvar_empresas(empresas):
    """Salva o dicionário de empresas no arquivo JSON com formatação legível."""
    try:
        with open(ARQUIVO_DB, "w", encoding="utf-8") as f:
            json.dump(empresas, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Erro ao salvar dados: {e}")