from datetime import datetime, timedelta


class Emprestimo:
    def __init__(self, idEmprestimo, idUsuario, idItem, StatusEmprestimo):
        self.idEmprestimo = idEmprestimo
        self.usuario = idUsuario
        self.item = idItem
        self.StatusEmprestimo = StatusEmprestimo
        self.dataEmprestimo = datetime.now()
        self.dataDevolucaoPrevista = None
        self.dataDevolucaoReal = None

    def concluir(self):
        self.StatusEmprestimo = "CONCLUIDO"
        self.dataDevolucaoReal = datetime.now()

    def renovar(self, dias):
        self.dataDevolucaoPrevista += timedelta(days=dias)
