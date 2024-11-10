from models.emprestimo import Emprestimo

class BibliotecaController:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def realizar_emprestimo(self, usuario, livro):
        if livro.disponivel:
            emprestimo = Emprestimo(usuario, livro)
            usuario.emprestimos.append(emprestimo)
            livro.disponivel = False
        else:
            print("Livro indisponível para empréstimo.")
