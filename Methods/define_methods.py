class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def exibir_detalhes(self):
    print(f"A marca do carro é {self.marca} o modelo é {self.modelo} e o ano é {self.ano}")


carro_novo = Carro("Toyota", "Corolla", "2024")
carro_novo.exibir_detalhes()