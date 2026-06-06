print(40*'-')
#sorteio de nome 
import random
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))             
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
escolhido = random.choice([n1, n2, n3, n4]) #escolhe um nome aleatório dentro da lista []
print('O aluno escolhido foi {}'.format(escolhido))


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

