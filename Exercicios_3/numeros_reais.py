'''
• Faça um programa que lê 4 números reais em uma
lista, calcula e exibe a quantidade de números
negativos e a soma dos números positivos dessa
mesma lista;
'''
#Opção 1
reais = []
positivos = []
negativos = 0

print("Digite quatro números reais!\n")
for i in range(4):
	reais.append(int(input()))

#negativos é o contador de números negativos
#se o número for maior que zero (positivo) o programa guarda numero na lista de positivos
for numero in reais:
	if numero < 0:
		negativos += 1
	elif numero > 0:
		positivos.append(numero)

print("A soma dos números positivos é:",sum(positivos))
print("A quantidade de números negativos é:",negativos)

'''
#Opção 2
reais = []
soma_positivos = 0
negativos = 0

print("\nDigite quatro números reais!\n")
for i in range(4):
	reais.append(int(input()))

#soma de positivos como uma variável
for numero in reais:
	if numero < 0:
		negativos += 1
	elif numero > 0:
		soma_positivos = soma_positivos + numero

print("A soma dos números positivos é:",soma_positivos)
print("A quantidade de números negativos é:",negativos)
'''
