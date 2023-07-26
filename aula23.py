"""//TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).//

//TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.//

//TODO: Imprimir a saída no formato especificado neste desafio.//
"""

valorHamburguer = float(input("Digite o valor do hamburghuer: "))
quantidadeHamburguer = int(input("Digite a quantidade de hambugueres:"))
valorBebida = float(input(" Digite o valor da Bebida: "))
quantidadeBebida = int(input("Digite a quantidade de Bebidas: "))
valorPago = float(input("Digite o valor Pago: "))

# Calcular o preço final do pedido
precoFinal = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)

# Calcular o troco
troco = valorPago - precoFinal

# Imprimir a saída
print(f"preço final: {precoFinal: .2f}")
print(f"troco Final: {troco: 2f} ")
      
