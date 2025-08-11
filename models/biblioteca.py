class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros(self):
        try:
            if not self.livros:
                print("Nenhum livro cadastrado.")
            else:
                for livro in self.livros:
                    print(livro)
        except Exception as e:
            print(f"Erro ao listar livros: {e}")
