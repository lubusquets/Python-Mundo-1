#manipulação de cadeia de texto

frase = "Curso em Vídeo Python"
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
print(frase.replace('Python', 'Android')) #imprime a frase substituindo a palavra 'Python' por 'Android'
print(frase.upper()) #imprime a frase toda em maiúsculo
print(frase.lower()) #imprime a frase toda em minúsculo
print(frase.capitalize()) #imprime a frase com a primeira letra maiúscula e as
restantes minúsculas
print(frase.title()) #imprime a frase com a primeira letra de cada palavra maiúscula
print(frase.strip()) #imprime a frase sem os espaços no início e no final
print(frase.rstrip()) #imprime a frase sem os espaços no final
print(frase.lstrip()) #imprime a frase sem os espaços no início
print(frase.split()) #imprime a frase dividida em uma lista de palavras
print('-'.join(frase)) #imprime a frase com os caracteres '-' entre as letras

