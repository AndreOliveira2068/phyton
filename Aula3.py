nome = "andre crispim"
altura = 1.70
peso = 75
Imc = peso / (altura * altura)

linha_1 = f' {nome} tem {altura:.2f} de altura',
linha_2 = f' pesa {peso} quilos e seu imc é'
linha_3 = f'{Imc: .2f}'

print(linha_1)
print(linha_2)
print(linha_3)

