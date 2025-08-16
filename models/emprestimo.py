from datetime import datetime, timedelta


class Emprestimo:
    def __init__(self, idEmprestimo, usuario, item, StatusEmprestimo):
        self.idEmprestimo = idEmprestimo
        self.usuario = usuario
        self.item = item
        self.StatusEmprestimo = StatusEmprestimo
        self.dataEmprestimo = datetime.now()
        self.dataDevolucaoPrevista = None
        self.dataDevolucaoReal = None

    def concluir(self):
        self.StatusEmprestimo = "CONCLUIDO"
        self.dataDevolucaoReal = datetime.now()

    def renovar(self, dias):
        self.dataDevolucaoPrevista += timedelta(days=dias)
