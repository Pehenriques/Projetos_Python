from usuario import Usuario as user
from replit import clear

list_user = []

def menu():
    print("Escolha uma opção: \n")
    print("[1] - Criar Usuário")
    print("[2] - Deletar Usuário")
    print("[3] - Atualizar Usuário")
    print("[4] - Listar Usuários")
    print("[5] - Sair\n")
    return input("Digite uma opção: ")


def valid_option(opcao):
    if opcao.isnumeric() and 0 < int(opcao) <= 5:
        return False
    return True


def valid_menu_value():
    valid_value = menu()
    while valid_option(valid_value):
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
        valid_value = menu()
    return int(valid_value)


def criar_usuario():
    print("<<<<<<<<>>>>>>>>")
    nome = input("Digite o nome do Usuário: ")
    email = input("Digite o e-mail do Usuário: ")
    telefone = input("Digite o telefone do Usuário: ")
    print("<<<<<<<<>>>>>>>>")
    return user(nome, email, telefone)


def salva_usuario(user):
    list_user.append(user)


def buscar_usuario(nome):
    for user in list_user:
        if user.get_nome() == nome:
            return user
    return None


def listar_usuarios():
    if len(list_user) > 0:
        for user in list_user:
            print(f"Nome: {user.get_nome()}")
            print(f"E-mail: {user.get_email()}")
            print(f"Telefone: {user.get_telefone()}")
            print("------------")
    else:
        print("Nenhum usuário cadastrado")


def deletar_usuario(nome):
    user = buscar_usuario(nome)
    if user:
        list_user.remove(user)
        print(f"Usuário {nome} removido com sucesso")
    else:
        print("Usuário inválido")


def menu_atualizar():
    print("1 - Atualizar nome")
    print("2 - Atualizar email")
    print("3 - Atualizar telefone")
    print("4 - Sair\n")


def atualizar_usuario():
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


def main():
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