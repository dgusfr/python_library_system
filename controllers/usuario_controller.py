from models.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome, idade):
        novo_usuario = Usuario(nome, idade)
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def listar_usuarios(self):
        return self.usuarios

    def remover_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome == nome:
                self.usuarios.remove(usuario)
                return usuario
        return None
