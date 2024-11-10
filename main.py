from controllers.biblioteca_controller import BibliotecaController

def exibir_menu():
    print("1. Adicionar Livro")
    print("2. Adicionar Usuário")
    print("3. Realizar Empréstimo")
    print("4. Devolver Livro")
    print("5. Sair")

def menu_principal():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            # Adicionar lógica para adicionar livro
            pass
        elif opcao == '2':
            # Adicionar lógica para adicionar usuário
            pass
        elif opcao == '3':
            # Adicionar lógica para realizar empréstimo
            pass
        elif opcao == '4':
            # Adicionar lógica para devolução
            pass
        elif opcao == '5':
            print("Encerrando o sistema...")
            break
