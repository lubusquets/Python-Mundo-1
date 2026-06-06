print(40*'-')
#sorteio de nome 
from random import choice
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))             
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1,n2,n3,n4]
escolhido = choice(lista) #escolhe um nome aleatório dentro da lista []
print('O aluno escolhido foi {}'.format(escolhido))

print(40*'-')
#novo sorteio organizado

import random
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1,n2,n3,n4]
escolhido = random.sample(lista,4) #escolhe um nome e organiza em até 4 posições sem repetir nomes
print('O primeiro aluno escolhido foi {}'.format(escolhido[0]))
print('O segundo aluno escolhido foi {}'.format(escolhido[1]))
print('O terceiro aluno escolhido foi {}'.format(escolhido[2]))
print('O quarto aluno escolhido foi {}'.format(escolhido[3]))

#ou mais simples ainda
import random
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1,n2,n3,n4]
random.shuffle(lista) #organiza a lista de forma aleatória
print('A ordem de apresentação será ')
print(lista)
