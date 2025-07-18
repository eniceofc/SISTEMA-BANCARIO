import json

def salvar_dados(usuarios, contas):
    """Salva os dados de usuários e contas em um arquivo JSON."""
    # Junta tudo em um único dicionário para salvar
    dados = {"usuarios": usuarios, "contas": contas}
    with open("banco_dados.json", "w", encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("\n[Sistema] Dados salvos com sucesso!")

def carregar_dados():
    """Carrega os dados de usuários e contas do arquivo JSON."""
    try:
        with open("banco_dados.json", "r", encoding='utf-8') as f:
            dados = json.load(f)
            return dados["usuarios"], dados["contas"]
    except FileNotFoundError:      
        return [], []
    except json.JSONDecodeError:
        return [], []