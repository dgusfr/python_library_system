from datetime import datetime

class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def __len__(self):
    ano_atual = datetime.now().year
    return ano_atual - self.ano


carro_novo = Carro("Toyota", "Corolla", 2017)
print(len(carro_novo))

