from conta.usuario import filtrar_usuario
from conta.config import LIMITE_SAQUE, LIMITE_SAQUES_DIARIOS

def criar_conta_corrente(contas, usuarios):
    
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        numero_conta = len(contas) + 1
        
        nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0.0,
        "extrato": "",
        "numero_saques": 0,
        "limite": LIMITE_SAQUE,
        "limite_saques": LIMITE_SAQUES_DIARIOS
        }
        
        contas.append(nova_conta)
        print("\n=== Conta criada com sucesso! ===")
        print(f"Agência: {nova_conta['agencia']} | Conta: {nova_conta['numero_conta']} | Titular: {usuario['nome']}")
    else:
        print("\n@@@ Usuário não encontrado Não é possível abrir a conta. @@@")