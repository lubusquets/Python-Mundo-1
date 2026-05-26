#exercício1
print('Olá,Mundo!') #ou utilize
msg = 'Olá,Mundo!'
print(msg)

#exercício2
print(4+7) #sem aspas ele soma os números, com aspas ele concatena as strings
print('4'+'7')

#exercício3
nome = input('Digite seu nome: ')
print('Olá', nome,'é um prazer te conhecer!') #ou utilize a opção abaixo
print('É um prazer te conhecer, {}'.format(nome))

#exercício4
dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')
print('Você nasceu no dia', dia, 'do mês', mes, 'do ano', ano,'.Correto?')

#exercício5
num = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
soma = num + num2
print('A soma dos números é:', soma)

