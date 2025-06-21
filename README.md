# Sistema Bancário Simples em Python

Este é um projeto de um sistema bancário básico desenvolvido em Python. Ele simula as operações essenciais de uma conta bancária através de um menu interativo no console (CLI - Command-Line Interface).

## 📜 Descrição

O sistema permite que um usuário realize depósitos, saques e visualize o extrato de uma única conta. Foi desenvolvido de forma modular, separando as responsabilidades em diferentes arquivos para facilitar a manutenção e o entendimento do código.

## ✨ Funcionalidades

O menu principal oferece as seguintes opções:

  * **[d] Depositar:** Adiciona um valor ao saldo da conta.
  * **[s] Sacar:** Retira um valor do saldo da conta, sujeito a regras específicas.
  * **[e] Extrato:** Exibe o histórico de transações (depósitos e saques) e o saldo atual.
  * **[q] Sair:** Encerra a aplicação.

## 룰 Regras de Negócio para Saque

A operação de saque possui as seguintes condições, que são validadas a cada tentativa:

1.  **Limite de Saldo:** O valor do saque não pode ser maior que o saldo disponível na conta.
2.  **Limite por Operação:** O valor máximo para cada saque é de **R$ 500,00**.
3.  **Limite de Quantidade:** O usuário pode realizar no máximo **3 saques** por sessão.

## 🚀 Como Executar

### Pré-requisitos

  * Python 3 instalado em sua máquina.

### Passos

1.  Clone ou faça o download dos arquivos do projeto para o seu computador.

2.  Abra um terminal (ou Prompt de Comando) e navegue até a pasta raiz do projeto.

3.  Execute o arquivo principal com o seguinte comando:

    ```bash
    python main.py
    ```

4.  O menu interativo será exibido. Siga as instruções e digite a letra correspondente à operação desejada.

## 📂 Estrutura dos Arquivos

O projeto está organizado da seguinte maneira para garantir a separação de responsabilidades:

```
/
├── main.py
└── conta/
    ├── __init__.py
    ├── config.py
    ├── conta.py
    └── operacoes.py
```

  * `main.py`: Arquivo principal que inicia o programa, exibe o menu e gerencia a interação com o usuário.
  * `conta/`: Pacote que agrupa todos os módulos relacionados à lógica da conta bancária.
  * `conta/config.py`: Armazena as variáveis de configuração e constantes, como os limites de saque e as mensagens padrão do sistema.
  * `conta/conta.py`: Contém a função `criar_conta()`, responsável por inicializar o dicionário que representa a conta com seus valores padrão.
  * `conta/operacoes.py`: Contém a lógica de negócio para as operações de `depositar()`, `sacar()` e `ver_extrato()`.

-----

## 💡 Próximas melhorias
 Salvar dados em JSON

 Suporte a múltiplas contas

 Refatorar usando orientação a objetos (POO)

 Interface gráfica com Tkinter ou Web com Flask

## 🧠 Aprendizados
Este projeto foi desenvolvido como parte dos meus estudos no Bootcamp Santander 2025 - Back-End com Python (DIO), com o objetivo de praticar:

Lógica de programação

Modularização com funções e arquivos

Tratamento de exceções
