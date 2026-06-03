import math #ou from math import hypot
c_oposto = float(input("Digite o valor do cateto oposto: "))
c_adjacente = float(input("Digite o valor do cateto adjacente: "))
h = math.hypot(c_oposto, c_adjacente)
print('A hipotenusa é igual a {:.2f}'.format(h))

