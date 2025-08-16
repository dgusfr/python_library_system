from abc import ABC, abstractmethod


class ItemAcervo(ABC):
    def __init__(self, id, titulo, anoPublicacao, status):
        self.id = id
        self.titulo = titulo
        self.anoPublicacao = anoPublicacao
        self.status = status

    @abstractmethod
    def descrever(self):
        pass
