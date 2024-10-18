class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def __str__(self):
    return f"A marca do carro é {self.marca} o modelo é {self.modelo} e o ano é {self.ano}"


carro_novo = Carro("Toyota", "Corolla", "2024")
print(carro_novo)