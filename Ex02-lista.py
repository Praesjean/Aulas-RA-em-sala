#Crie um algoritmo que peça ao usuário para informar 5 valores inteiros positivos e armazene-os em uma lista com nome qualquer.
#Em seguida, crie uma nova lista ordenada dos valores e uma nova lista com os valores ordenados em ordem inversa.
#Imprima na tela:
#a. As três listas
#b. O tamanho da lista
#c. O menor valor informado
#d. O maior valor informado
#e. A soma de todos os valores da lista

lista = []

for i in range(5):
    numeros = int(input(f"Informe o {i+1}° número: "))
    i += 1
    lista.append(numeros)

print(lista)
