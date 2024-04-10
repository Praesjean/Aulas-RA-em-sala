#Imprimir os elementos de um vetor qualquer
#Criando um vetor
escalacao = ['Everson','Gui Arana','M. Lemos','B. Fuchs','Saravia','Rubens','Battaglia','G. Scarpa','Zaracho','Paulinho','Hulk']
for jogadores in escalacao:
    print(jogadores)

#Vamos fazer a mesma coisa
#Fazendode outra forma (caso precise do indice)
for i in range(0,len(escalacao)):
    print(f"Elemento {i+1}: Valor: {escalacao[i]}")