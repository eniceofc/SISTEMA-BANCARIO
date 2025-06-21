from conta.config import *



def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(MENSAGEM_VALOR_INVALIDO)



def sacar(conta, valor):
    saldo = conta["saldo"]
    limite = conta["limite"]
    numero_saques = conta["numero_saques"]
    LIMITE_SAQUES = conta["limite_saques"] # No seu código original estava em maiúsculo, mantive o padrão
    
    # Importando as mensagens para dentro da função para garantir que estão acessíveis
    from conta.config import MENSAGEM_SALDO_INSUFICIENTE, MENSAGEM_LIMITE_EXCEDIDO, MENSAGEM_SAQUES_EXCEDIDOS, MENSAGEM_VALOR_INVALIDO

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print(MENSAGEM_SALDO_INSUFICIENTE)

    elif excedeu_limite:
        print(MENSAGEM_LIMITE_EXCEDIDO)

    elif excedeu_saques:
        print(MENSAGEM_SAQUES_EXCEDIDOS)

    elif valor > 0:
        # Se chegou até aqui, o saque é válido.
        # As linhas abaixo eram a causa do erro original.
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    else:
        print(MENSAGEM_VALOR_INVALIDO)
    

    

def ver_extrato(conta):
    print("\n================ EXTRATO ================")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        print(conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")
