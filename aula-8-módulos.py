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
#import emoji    por algum motivo que não consegui descobrir e resolver este código não está funcionando *preciso rever.
#print(emoji.emojize('Python é :thumbs_up:')) 

from math import trunc
num = float(input("Digite um número decimal: "))
print('O número {} tem a a parte inteira {}'.format(num, trunc(num)))
print(40*'-')

'''ou
import math
num = float(input("Digite um número decimal: "))
print('O número {} tem a a parte inteira {}'.format(num, math.trunc(num)))

ou ainda
num = float(input("Digite um número decimal: "))
print('O número {} tem a a parte inteira {}'.format(num, int(num)))'''




