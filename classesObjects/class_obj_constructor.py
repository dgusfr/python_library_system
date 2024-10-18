class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

    print(f"A marca do carro é {marca} o modelo é {modelo} e o ano é {ano}")


carro_novo = Carro("Toyota", "Corolla", "2024")
