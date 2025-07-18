from conta.config import *
from conta.usuario import criar_usuario
from conta.contas import criar_conta_corrente
from conta.operacoes import depositar, sacar, ver_extrato
from conta.dados import *


def exibir_menu():
    menu = """
    ================ MENU ================
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nc]Nova conta
    [lc]Listar contas
    [nu]Novo usuário
    [q]\tSair
    => """
    return input(menu).lower()

def buscar_conta_cliente(numero_conta, contas):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            return conta
    return None

def main():
    usuarios, contas = carregar_dados()


    while True:
        opcao = exibir_menu()
        
        if opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            criar_conta_corrente(contas, usuarios)
        
        elif opcao == "lc":
            print("\n================ CONTAS ================")
            if not contas:
                print("Nenhuma conta cadastrada.")
            for conta in contas:
                print(f"Agência: {conta['agencia']}\tC/C: {conta['numero_conta']}\tTitular: {conta['usuario']['nome']}")
            print("==========================================")

        elif opcao == "d":
            numero_conta = int(input("Informe o número da conta para depósito: "))
            conta = buscar_conta_cliente(numero_conta, contas)
            
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                
                novo_saldo, novo_extrato = depositar(conta['saldo'], valor, conta['extrato'])
                
                conta['saldo'] = novo_saldo
                conta['extrato'] = novo_extrato
            else:
                print("@@@ Conta não encontrada! @@@")

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta para saque: "))
            conta = buscar_conta_cliente(numero_conta, contas)
            
            if conta:
                valor = float(input("informe o valor do saque: "))
                
                novo_saldo, novo_extrato, novo_num_saques = sacar(
                    saldo = conta['saldo'],
                    valor = valor,
                    extrato = conta['extrato'],
                    limite= conta['limite'],
                    numero_saques = conta['numero_saques'],
                    limite_saques = LIMITE_SAQUES_DIARIOS
                )
                conta['saldo'] = novo_saldo
                conta['extrato'] = novo_extrato
                conta['numero_saques'] = novo_num_saques
            else:
                print("@@@ Contas não encontradas! @@@")

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta para ver o extrato: "))
            conta = buscar_conta_cliente(numero_conta, contas)
            
            if conta:
                ver_extrato(conta['saldo'],  extrato = conta['extrato'])
            else:
                print("@@@ Conta não encontrada! @@@")

        elif opcao == "q":
            salvar_dados(usuarios, contas)
            print("\nObrigado por usar o sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida. Tente novamente.")


if __name__ == "__main__":
    main()