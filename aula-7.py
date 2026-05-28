print('Exercício 1')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma dos números é igual a {}'.format(n1+n2)) 
print(40*'-')

print('Exercício 2')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, a multiplicação é {} e a divisão é {:.3f}'.format(s, m, d), end=' - ') #o {:.3f} formata a saída para 3 casas decimais - F de números flutuantes. End =' ' é para não quebrar a linha, ou seja, continuar na mesma linha
print('A divisão inteira é {} e a potência é {}'.format(di, e))
print(40*'-')

print('Exercício 3')
n1 = int(input('Digite um número: '))
ant = n1-1
suc = n1+1
print('O antecessor de {} é {} e o sucessor é {}'.format(n1,ant,suc))
#ATENÇÃO - SÓ REDUZA A QUANTIDADE DE VARIÁVEIS se não for utilizar posteriormente (isso economiza memória no programa), então faça:
#n1 = int(input('Digite um número: '))
#print('O antecessor de {} é {} e o sucessor é {}'.format(n1, n1-1, n1+1))
print(40*'-')

print('Exercício 4')
n1 = int(input('Digite um número: '))
d = n1*2
t = n1*3
r = n1**1/2
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n1,d,t,r))
print(40*'-')

print('Exercício 5') # calculadora de média
n = input('Nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A média de {} é {:.1f}'.format(n,m))
print(40*'-')

print('Exercício 6') #conversor de medidas
m = float(input('Digite a medida em metros: '))
cm = m*100
mm = m*1000
print('A medida de{}m corresponde a {} centímetros e {} milímetros'.format(m,cm,mm))
print(40*'-')











