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
        usuarioEncontrado = None
        for usuario in self.usuarios:
            if usuario.idUsuario == idUsuario:
                usuarioEncontrado == usuario
                break

        itemEcontrado = None
        for item in self.acervo:
            if item.id == idItem:
                itemEcontrado = item
                break

        if not usuarioEncontrado:
            print("Erro: Usuário não encontrado.")
            return None

        if not itemEcontrado:
            print("Erro: Item não encontrado.")
            return None

        if usuarioEncontrado.status != "ATIVO":
            print("Erro: O item não esta disponivél.")

        if itemEcontrado.status != "DISPONIVEL":
            print("Erro: O item não esta disponivél.")

        idEmprestimo = len(self.emprestimos) + 1
        StatusEmprestimo = "ATIVO"

        novoEmprestimo = Emprestimo(idEmprestimo, idUsuario, idItem, StatusEmprestimo)
        print("Emprestimo realizado com sucesso!")
        return novoEmprestimo

    def registrarDevolucao(self, idItem):
        for emprestimo in self.emprestimos:
            if idItem == emprestimo.id:
                emprestimo.concluir()
                return True

        return False

    def renovarEmprestimo(self, idEmprestimo):
        for emprestimo in self.emprestimos:
            if idEmprestimo == emprestimo:
                emprestimo.renovar()
                return True

        return False
