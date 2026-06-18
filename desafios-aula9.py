'''Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maiúsculas 
- o nome com todas as letras minúsculas
- quantas letras ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome'''

nome = input('Digite seu nome completo: ')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))  
print('Seu nome tem {} letras'.format(len(nome.strip())))
dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
print(50*'-')

'''Desafio 23 - Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
num = input('Digite um número entre 0 à 99999: ')
print('Unidade: {}'.format(num[3]))

print(50*'-')
'''Desafio 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'''

print(50*'-')
'''Desafio 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

print(50*'-')
'''Desafio 26 - Crie um programa que leia uma frase e diga quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

print(50*'-')
'''Desafio 27 - Crie um programa que leia o nome completo de uma pessoa e mostre:   - o primeiro nome   - o último nome'''  


