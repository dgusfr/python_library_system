class Usuario:
    def __init__(self, idUsuario, nome, email, StatusUsuario):
        self.idUsuario = idUsuario
        self.nome = nome
        self.email = email
        self.StatusUsuario = StatusUsuario

    def alterarStatus(self, novoStatus):
        self.StatusUsuario = novoStatus
