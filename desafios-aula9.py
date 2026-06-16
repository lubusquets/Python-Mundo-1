'''Crie um programa que leia o nome completo de uma pessoa e mostre:
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
