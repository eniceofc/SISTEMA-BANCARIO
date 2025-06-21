from conta.conta import criar_conta
from conta.operacoes import depositar, sacar, ver_extrato


def menu():
    return """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """


def main():
    conta = criar_conta()  # Cria conta com valores padrão do config

    while True:
        opcao = input(menu()).lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                depositar(conta, valor)
            except ValueError:
                print("Operação falhou! Digite um número válido.")

        # MUDANÇA SUGERIDA NO main.py PARA DEBUGAR
        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                sacar(conta, valor)
            except ValueError as e: # Adicionamos "as e"
                print("\n--- DEBUG ---")
                print("Ocorreu um ValueError inesperado. Detalhes do erro:")
                print(e) # Isso vai imprimir a mensagem de erro real do Python
                print("--- FIM DO DEBUdG ---\n")

        elif opcao == "e":
            ver_extrato(conta)

        elif opcao == "q":
            print("\nObrigado por usar o sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida. Tente novamente.")


if __name__ == "__main__":
    main()
