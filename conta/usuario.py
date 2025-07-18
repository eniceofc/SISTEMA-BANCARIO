from datetime import datetime

def criar_usuario(usuarios):
    
    # 1. Pede o cpf e verifica se já existe
    cpf_digitado = input("Informe o CPF: ")
    # Remove os pontos e os traços para ter apenas os números
    cpf = cpf_digitado.replace(".", "").replace("-", "")
    
    # Validação extra: verificam se o que sobrou são realmente dígitos e se tem 11 caracteres
    
    if not cpf.isdigit() or len(cpf) != 11:
        print("\n@@@ CPF inválido! Formato não reconhecido. Tente novamente. @@@")
        return # Para a execução
    
    # 2. Agora, com o CPF limpo, verifica se ele já existe
    
    usuario_encontrado = filtrar_usuario(cpf, usuarios) #Usa a  função de filtro
    
    if usuario_encontrado:
        print("\n@@@ Erro: Já existe um usuário com este CPF! @@@")
        return # Para a execução da fução e não cadastra ninguém
    
    # 3. Caso não encontre, pede o resto dos dados
    while True:
        nome = input("Informe o nome completo")
        if not nome:
            print("@@@ Erro: O nome não pode ficar em branco. @@@")
        elif len(nome.split()) < 2:
            print("@@@ Erro: Por favor, informe o nome e sobrenome. @@@")
        else:
            break
    while True:
        
        data_nascimento_str = input("Informe a data de nascimetno (dd-mm-aaaa): ")
        try:
            
            datetime.strptime(data_nascimento_str, "%d-%m-%Y")
            break
        except ValueError:
            print("\n@@@ Data inválida! Use o formato dd-mm-aaaa. @@@")
    while True:
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado)")
        if not endereco:
            print("\n@@@ Data inválida! Use o formato dd-mm-aaaa. @@@") 
        else:
            break         
    
    # 4. Cria o discionário novo usuário
    novo_usuario = {
        "nome":nome,
        "data_nascimento": data_nascimento_str,
        "cpf":cpf,
        "endereco": endereco
    }
    
    # 5. Adiciona o novo usuário na lista 
    
    usuarios.append(novo_usuario)
    print("\n=== Usuário criado com sucessso! ===")
    
def filtrar_usuario(cpf, usuarios):
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            
            return usuario
    return None