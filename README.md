# Sistema Bancário v2.0 em Python

Este projeto é a evolução de um sistema bancário básico, desenvolvido em Python. Ele simula as operações essenciais de um banco através de um menu interativo no console (CLI - Command-Line Interface), agora com suporte a múltiplos usuários, múltiplas contas e persistência de dados.

## 📜 Descrição

O sistema foi refatorado para uma arquitetura modular, separando as responsabilidades em diferentes arquivos para facilitar a manutenção e o entendimento do código. Ele agora permite o cadastro de clientes e a criação de contas correntes vinculadas a eles, com todos os dados sendo salvos em um arquivo `json` para que as informações não se percam ao fechar o programa.

## ✨ Funcionalidades

O menu principal oferece as seguintes opções:

  * **[nu] Novo Usuário:** Cadastra um novo cliente no sistema.
  * **[nc] Nova Conta:** Cria uma nova conta corrente vinculada a um usuário existente.
  * **[lc] Listar Contas:** Exibe todas as contas cadastradas.
  * **[d] Depositar:** Adiciona um valor ao saldo de uma conta específica.
  * **[s] Sacar:** Retira um valor do saldo de uma conta, sujeito a regras.
  * **[e] Extrato:** Exibe o histórico de transações e o saldo atual de uma conta.
  * **[q] Sair:** Encerra a aplicação e salva todas as alterações.

## 룰 Regras de Negócio para Saque

A operação de saque possui as seguintes condições, que são validadas a cada tentativa:

1.  **Limite de Saldo:** O valor do saque não pode ser maior que o saldo disponível.
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

O projeto foi reestruturado para garantir a separação de responsabilidades:

```
/
├── main.py
├── banco_dados.json
└── conta/
    ├── __init__.py
    ├── config.py
    ├── contas.py
    ├── usuario.py
    └── operacoes.py
```

  * `main.py`: Arquivo principal que inicia o programa, exibe o menu e gerencia a interação com o usuário, além de carregar e salvar os dados.
  * `banco_dados.json`: Arquivo que armazena os dados dos usuários e contas.
  * `conta/`: Pacote que agrupa todos os módulos relacionados à lógica do sistema.
  * `conta/config.py`: Armazena as constantes, como os limites de saque e mensagens padrão.
  * `conta/usuario.py`: Contém as funções para criar e buscar usuários.
  * `conta/contas.py`: Contém a função para criar contas correntes.
  * `conta/operacoes.py`: Contém a lógica de negócio para `depositar()`, `sacar()` e `ver_extrato()`.

-----

## ✅ Melhorias Implementadas

  * **Salvar dados em JSON:** Os dados agora são persistidos, evitando a perda de informações.
  * **Suporte a múltiplos usuários e contas:** O sistema não está mais limitado a uma única conta.
  * **Modularização completa:** O código foi refatorado e organizado em funções e módulos com responsabilidades únicas.
  * **Validação de Entradas:** Foram adicionadas validações para CPF, data de nascimento e outros campos de usuário.

## 🧠 Aprendizados

Este projeto foi desenvolvido e refatorado como parte dos meus estudos no Bootcamp Santander 2024 - Back-End com Python (DIO), com o objetivo de praticar:

  * Lógica de programação e algoritmos.
  * Modularização com funções e pacotes Python.
  * Manipulação de estruturas de dados (listas e dicionários).
  * Persistência de dados com o módulo `json`.
  * Versionamento de código com Git e GitHub.
  * Depuração de código e tratamento de exceções.