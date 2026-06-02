import math  #ou from math import (crt+espaço)sqrt
num = int(input("Digite um número: "))
raiz = math.sqrt(num) #no segundo caso utilize apenas sqrt nesta linha, sem math
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))    
# arredondar a resposta para cima .format(num, math.ceil(raiz)))
# arredondar a resposta para baixo .format(num, math.floor(raiz)))

print(40 * '-')

import random
num = random.randint(1, 10) #gera um número aleatório entre 1 e 10
print(num)

print(40 * '-')