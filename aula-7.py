print('Exercício 1')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma dos números é igual a {}'.format(n1+n2)) 

print(20*'-')

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












