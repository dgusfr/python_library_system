class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.emprestimos = []

    def __str__(self):
        return f"Usuário: {self.nome}, Email: {self.email}"
