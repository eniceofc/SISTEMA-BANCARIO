from conta.config import *

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += (f"Depósito: R$ {valor:.2f}\n")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(MENSAGEM_VALOR_INVALIDO)
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print(MENSAGEM_SALDO_INSUFICIENTE)

    elif excedeu_limite:
        print(MENSAGEM_LIMITE_EXCEDIDO)

    elif excedeu_saques:
        print(MENSAGEM_SAQUES_EXCEDIDOS)

    elif valor > 0:

        saldo -= valor
        extrato += (f"Saque: R$ {valor:.2f}\n")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    else:
        print(MENSAGEM_VALOR_INVALIDO)
    return saldo, extrato, numero_saques




def ver_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    Recebe saldo por posição e extrato por nome.
    """
    print("\n================ EXTRATO ================")
    # Verifica se a string do extrato está vazia
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato) # Se não estiver vazia, imprime o histórico
    
    # Imprime o saldo final, formatado
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")