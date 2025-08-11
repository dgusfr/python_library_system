from models.biblioteca import Biblioteca
from models.livro import Livro
from models.usuario import Usuario


def exibir_menu():
    print("\n===== Sistema de Biblioteca =====")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Remover Livro")
    print("4. Adicionar Usuário")
    print("5. Listar Usuários")
    print("6. Remover Usuário")
    print("7. Realizar Empréstimo")
    print("8. Registrar Devolução")
    print("9. Sair")


def menu():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano = input("Digite o ano de publicação do livro: ")
                livro = Livro(titulo, autor, ano)
                biblioteca.adicionar_livro(livro)
                print("Livro adicionado com sucesso.")
            case "2":
                biblioteca.listar_livros()
            case "3":
                titulo = input("Digite o título do livro a ser removido: ")
                biblioteca.remover_livro(titulo)
            case "4":
                nome = input("Digite o nome do usuário: ")
                idade = input("Digite a idade do usuário: ")
                usuario = Usuario(nome, idade)
                biblioteca.adicionar_usuario(usuario)
                print("Usuário adicionado com sucesso.")
            case "5":
                biblioteca.listar_usuarios()
            case "6":
                nome = input("Digite o nome do usuário a ser removido: ")
                biblioteca.remover_usuario(nome)
            case "7":
                titulo = input("Digite o título do livro para empréstimo: ")
                nome = input("Digite o nome do usuário que fará o empréstimo: ")
                biblioteca.realizar_emprestimo(titulo, nome)
            case "8":
                titulo = input("Digite o título do livro a ser devolvido: ")
                biblioteca.registrar_devolucao(titulo)
            case "9":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
