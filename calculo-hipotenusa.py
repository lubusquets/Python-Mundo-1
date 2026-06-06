import math #ou from math import hypot
c_oposto = float(input("Digite o valor do cateto oposto: "))
c_adjacente = float(input("Digite o valor do cateto adjacente: "))
h = math.hypot(c_oposto, c_adjacente)
print('A hipotenusa é igual a {:.2f}'.format(h))

'''ou
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
h = (co**2 + ca**2)**1/2
print('A hipotenusa é igual a {:.2f}'.format(h))
''' 
print(40*'-')
#cálculo de seno, cosseno e tangente

from math import radians, sin, cos, tan
angulo = float(input("Digite o valor do ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {} é {:.2f}'.format(angulo, seno))
print('O cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))

print(40*'-')
#sorteio de nome 
import random
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))             
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
escolhido = random.choice([n1, n2, n3, n4]) #escolhe um nome aleatório dentro da lista []
print('O aluno escolhido foi {}'.format(escolhido))

