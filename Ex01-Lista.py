#Crie um algoritmo que possua duas listas vazias chamadas numerosJogador1 e numerosJogador2.
#Em seguida, randomize um número entre 1 e 6 (vamos simular um dado) e armazene o valor na lista.
#Repita esse processo 3 vezes (como se 3 dados tivessem sido jogados) para cada um dos jogadores.
#Por último, some os valores de cada jogador, e exiba na tela qual jogador foi o vencedor.
#Vence aquele quetiver a soma com maior número.
import random

numerosJogador1 = []
numerosjogador2 = []
somajogador1 = 0
somajogador2 = 0

for i in range(3):
    numeros1 = random.randint(1,6)
    numerosJogador1.append(numeros1)
    somajogador1 += numeros1
    numeros2 = random.randint(1,6)
    numerosjogador2.append(numeros2)
    somajogador2 += numeros2

print(numerosJogador1)
print(numerosjogador2)
print(f"A soma do Jogador 1 é: {somajogador1}")
print(f"A soma do Jogador 2 é: {somajogador2}")

if somajogador1 > somajogador2:
    print("Jogador 1 venceu")

elif somajogador1 == somajogador2:
    print("Deu empate")

else:
    print("Jogador 2 venceu")

#Crie um algoritmo que peça ao usuário para informar 5 valores inteiros positivos e armazene-os em uma lista com nome qualquer.
#Em seguida, crie uma nova lista ordenada dos valores e uma nova lista com os valores ordenados em ordem inversa.
#Imprima na tela:
#a. As três listas
#b. O tamanho da lista
#c. O menor valor informado
#d. O maior valor informado
#e. A soma de todos os valores da lista

