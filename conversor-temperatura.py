print('        CONVERSOR DE TEMPERATURA        ')
print(50*'-')

c = float(input('Digite a temperatura em °C: '))
f = (c*9/5)+32 #aqui pode usar sem parenteses, pois já está na ordem de precedência, mas é recomendado usar para facilitar a leitura.
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F.'.format(c,f))
