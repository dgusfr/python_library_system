class Carro:
  def __init__(self):
    self.marca = None
    self.modelo = None
    self.ano = None


carro_novo = Carro()
carro_novo.marca = "Toyota"
carro_novo.modelo = "Corolla"
carro_novo.ano = "2024"

print(f"A marca do carro é {carro_novo.marca} o modelo é {carro_novo.modelo} e o ano é {carro_novo.ano}")