'''Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maiúsculas 
- o nome com todas as letras minúsculas
- quantas letras ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))  
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))

print(50*'-')

'''Desafio 23 - Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
num = int(input('Digite um número entre 0 à 99999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
