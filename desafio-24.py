'''Desafio 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
#print(cidade[:5].upper() == 'SANTO')
print('SANTO' in cidade.upper()) #prefiro este código que encontra a palavra em qualquer posição do nome da cidade, e não apenas no início.

print(50*'-')
'''Desafio 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input('Digite seu nome completo: ').strip())
print('SILVA' in nome.upper())
# print('silva' in nome.lower()) 

print(50*'-')
'''Desafio 26 - Crie um programa que leia uma frase e diga quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('A') + 1))

'''ou de maneira maos somples:
frase = str(onput('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('A') + 1))
'''

print(50*'-')
'''Desafio 27 - Crie um programa que leia o nome completo de uma pessoa e mostre:   - o primeiro nome   - o último nome'''  

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu primeiro nome é: {}'.format(dividido[0]))
print('Seu último nome é: {}'.format(dividido[len(dividido)-1]))

