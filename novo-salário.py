print('           NOVO SALÁRIO        ')
print(30*'*')

n = (input('Digite o nome do funcionário: '))
s = float(input('Digite o salário atual: R$ '))
sn = float(s*0.15) #15% de aumento
#ou sn = s+(s*15/100) lembrando de alterar o format.
print('O novo salário de {} é R${:.2f}.'.format(n,s+sn))



