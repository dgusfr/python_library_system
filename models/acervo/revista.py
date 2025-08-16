from acervo.item_acervo import ItemAcervo


class Revista(ItemAcervo):
    def __init__(self, id, titulo, anoPublicacao, status, edicao, periodicidade):
        super().__init__(id, titulo, anoPublicacao, status)
        self.edicao = edicao
        self.periodicidade = periodicidade

    def descrever(self):
        return f"A Revista {self.titulo} de periodicidade {self.periodicidade} foi adicionada ao acervo."
