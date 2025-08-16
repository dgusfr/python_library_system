from models import Emprestimo


class Biblioteca:
    def __init__(self):
        self.acervo = []
        self.usuarios = []
        self.emprestimos = []

    """
        +editarItem(string idItem, map dados) boolean
        +listarItens() List~ItemAcervo~
        +buscarItem(string termo) List~ItemAcervo~

        ---

        +editarUsuario(string idUsuario, map dados) boolean
        +listarUsuarios() List~Usuario~

        ---

        +realizarEmprestimo(string idUsuario, string idItem) Emprestimo
        +registrarDevolucao(string idItem) boolean
        +renovarEmprestimo(string idEmprestimo) boolean

    """

    def adicionarItem(self, item):
        self.acervo.append(item)

    def removerItem(self, idItem):
        for item in self.acervo:
            if idItem == item.id:
                self.acervo.remove(item)
                return True
        return False

    def cadastrarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def removerUsuario(self, idUsuario):
        for item in self.acervo:
            if idUsuario == item.id:
                self.acervo.remove(item)
                return True
        return False

    def realizarEmprestimo(self, idUsuario, idItem):
        novoEmprestimo = Emprestimo(idUsuario, idItem)
        self.emprestimos.append(novoEmprestimo)
        return novoEmprestimo
