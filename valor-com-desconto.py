print('VALOR COM DESCONTO')
print(40*'-')

v = float(input('Digite o valor do produto: '))
d = float(v*0.05) #5% de desconto
#ou d = v-(v*5/100) lembrando de alterar o format.
print('O valor do produto com desconto é R${:.2f}.'.format(v-d)) 



      
      
