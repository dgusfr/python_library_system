from datetime import datetime


class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def devolver(self):
        self.data_devolucao = datetime.now()
        self.livro.disponivel = True
