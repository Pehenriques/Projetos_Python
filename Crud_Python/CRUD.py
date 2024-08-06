from usuario import Usuario as user #import da classe usuario, e nomiei ela de user usando o 'as'
from replit import clear #import para limpar 

list_user = [] #Criei uma lista para receber os usuarios criados

def menu(): #Menu com as opções de funcionalidades do programa
    print("Escolha uma opção: \n")
    print("[1] - Criar Usuário")
    print("[2] - Deletar Usuário")
    print("[3] - Atualizar Usuário")
    print("[4] - Listar Usuários")
    print("[5] - Sair\n")
    return input("Digite uma opção: ")


def valid_option(opcao): #Função de validação das opções escolhidas 
    if opcao.isnumeric() and 0 < int(opcao) <= 5:
        return False
    return True


def valid_menu_value(): #Função de validação do menu
    valid_value = menu()
    while valid_option(valid_value):
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
        valid_value = menu()
    return int(valid_value)


def criar_usuario(): #Função de criar o usuario
    print("<<<<<<<<>>>>>>>>")
    nome = input("Digite o nome do Usuário: ")
    email = input("Digite o e-mail do Usuário: ")
    telefone = input("Digite o telefone do Usuário: ")
    print("<<<<<<<<>>>>>>>>")
    return user(nome, email, telefone)


def salva_usuario(user): #Função para salvar o usuario e adicionalo na lista
    list_user.append(user)


def buscar_usuario(nome): #Função para buscar o usuario dentro da lista
    for user in list_user:
        if user.get_nome() == nome:
            return user
    return None


def listar_usuarios(): #Função para listar usuario
    if len(list_user) > 0:
        for user in list_user:
            print(f"Nome: {user.get_nome()}")
            print(f"E-mail: {user.get_email()}")
            print(f"Telefone: {user.get_telefone()}")
            print("------------")
    else:
        print("Nenhum usuário cadastrado")


def deletar_usuario(nome): #Função para deletar usuario
    user = buscar_usuario(nome)
    if user:
        list_user.remove(user)
        print(f"Usuário {nome} removido com sucesso")
    else:
        print("Usuário inválido")


def menu_atualizar(): #Menu de atulização do atributo e componetes do usuario nome, email e telefone
    print("1 - Atualizar nome")
    print("2 - Atualizar email")
    print("3 - Atualizar telefone")
    print("4 - Sair\n")


def atualizar_usuario(): #Função para atualizar usuario 
    listar_usuarios()
    atualizar = input("Digite o nome do usuário que deseja atualizar: ")
    user = buscar_usuario(atualizar)
    if user is None:
        print("Usuário inválido")
        return
    while True:
        menu_atualizar()
        try:
            option = int(input("Digite uma opção: "))
        except ValueError:
            print("Opção inválida! Por favor, insira um número.")
            continue
        if option == 1:
            user.set_nome(input("Atualize o nome: "))
        elif option == 2:
            user.set_email(input("Atualize o email: "))
        elif option == 3:
            try:
                user.set_telefone(input("Atualize o telefone: "))
            except ValueError:
                print("Telefone inválido! Por favor, insira um número.")
        elif option == 4:
            break
        else:
            print("Opção inválida! Tente novamente.")


def main(): #Função main, aqui ela chama todas as funções dentro do loop onde enquanto ele estiver em funcinamento nas conseguimos utulizar todos os case Criar, atualizar, deletar e listar usuario
    while True:
        opcao_selecionada = valid_menu_value()
        match opcao_selecionada:
            case 1:
                clear()
                usuario = criar_usuario()
                salva_usuario(usuario)
            case 2:
                clear()
                usuario = input("Digite o nome do usuário que deseja excluir: ")
                deletar_usuario(usuario)
            case 3:
                clear()
                atualizar_usuario()
            case 4:
                clear()
                listar_usuarios()
            case 5:
                print("Saindo do programa")
                break


if __name__ == "__main__":
    main()