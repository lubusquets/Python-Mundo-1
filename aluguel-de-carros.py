print('        ALUGUEL DE CARROS        ')
print(40*'-')

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valor = (d*60) + (km*0.15)
print('O valor total do aluguel é R${:.2f}'.format(valor))

