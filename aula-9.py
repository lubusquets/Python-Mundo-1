#manipulação de cadeia de texto

frase = "   Curso em Vídeo Python  "
print(frase[3]) #imprime a letra na posição 3
print(frase[3:13]) #imprime da posição 3 até a posição 12
print(frase[:13]) #imprime da posição 0 até a posição 12
print(frase[1:15:2]) #imprime da posição 1 até a posição 14 pulando de 2 em 2
print(frase[::3]) #imprime toda a frase pulando de 3 em 3
print(frase.count('o')) #imprime quantas vezes a letra 'o' aparece  
print(frase.count('o', 0, 13)) #imprime quantas vezes a letra 'o' aparece da posição 0 até a posição 12
print(frase.find('deo')) #imprime a posição onde começa a palavra 'deo'
print(frase.find('Android')) #imprime -1 porque a palavra 'Android' não existe na frase
print('Curso' in frase) #imprime True porque a palavra 'Curso' existe na frase
print(frase.replace('Python', 'Android')) #imprime a frase substituindo a palavra 'Python' por 'Android' só neste momento.
#para usar o replace substituindo uma variável você deve usar:
'''frase = frase.replace('Python', 'Android')
print(frase)''' #isso vai substituir em todo o código

print(frase.upper()) #imprime a frase toda em maiúsculo
print(frase.upper().count('O')) #imprime quantas vezes a letra 'O' aparece na frase toda em maiúsculo
print(frase.lower()) #imprime a frase toda em minúsculo
print(frase.capitalize()) #imprime a frase com a primeira letra maiúscula e as restantes minúsculas
print(frase.title()) #imprime a frase com a primeira letra de cada palavra maiúscula
print(frase.strip()) #imprime a frase sem os espaços no início e no final
print(frase.rstrip()) #imprime a frase sem os espaços no final
print(frase.lstrip()) #imprime a frase sem os espaços no início
print(frase.split()) #imprime a frase dividida em uma lista de palavras
dividido = frase.split() #cria uma lista de palavras
print(dividido[0]) #imprime a primeira palavra da lista
print(dividido[2][3]) #imprime a terceira letra da lista

print('-'.join(frase)) #imprime a frase com os caracteres '-' entre as letras
print(len(frase)) #imprime o tamanho da frase, contando os espaços
print(len(frase.strip())) #imprime o tamanho da frase sem contar os espaços no início e no final

 



