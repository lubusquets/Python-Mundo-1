#tipos primitivos de variáveis
print('Exercício 1')
n1 = input('Digite um valor: ')#o tipo da variável é string, mesmo que seja um número, pois o input sempre retorna uma string
print(type(n1)) 
n2 = int(input('Digite outro valor: ')) #converte a string para inteiro, pois foi estipulado após o sinal de igual
print(type(n2))
print('--------------------------------------------------')

print('Exercício 2')
n1=input('Digite um número: ')
n2=input('Digite outro número: ')
soma = int(n1) + int(n2) #converte as strings para inteiros antes de somar
print('A soma entre 2.7os números {} e {} é: {}'.format(n1, n2, soma)) 
print('--------------------------------------------------')

print('Exercício 3')
n1 = float(input('Digite um número decimal (utilize ponto): ')) #converte a string para float, numeros flutuantes, com casas decimais
n2 = float(input('Digite outro número decimal: '))  
s = n1 + n2 
print('A soma entre os números {} e {} é igual a {}'.format(n1, n2, s))
print('--------------------------------------------------')

print('Exercício 4')
n1 = bool(input('Digite um número: ')) #converte a string para booleano, ou seja, verdadeiro ou falso
print (n1)
print('--------------------------------------------------')

print('Exercício 5')
n = input('Digite algo: ') 
print(n.isnumeric()) #verifica se a string é um número
n = input('Digite algo: ') 
print(n.isalpha()) #verifica se a string é uma  letra
n = input('Digite algo: ') 
print(n.isalnum()) #verifica se a string é alfanumérica, ou seja, letra ou número
n = input('Digite algo: ') 
print(n.isupper()) #verifica se a string é uma letra maiúscula















