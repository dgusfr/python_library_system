from acervo.item_acervo import ItemAcervo


class livro(ItemAcervo):
    def __init__(self, id, titulo, anoPublicacao, status, autor, isbn):
        super().__init__(id, titulo, anoPublicacao, status)
        self.autor = autor
        self.isbn = isbn

    def descrever(self):
        return f"O Livro {self.titulo} do autor {self.autor} foi adicionado ao acervo."
