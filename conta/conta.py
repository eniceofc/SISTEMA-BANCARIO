from conta.config import LIMITE_SAQUE, LIMITE_SAQUES_DIARIOS, MENSAGEM_LIMITE_EXCEDIDO

def criar_conta():
    return {
        "saldo": 0.0,
        "extrato": "",
        "numero_saques": 0,
        "limite": LIMITE_SAQUE,
        "limite_saques": LIMITE_SAQUES_DIARIOS
        
    }