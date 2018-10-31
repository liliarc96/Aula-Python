'''
• Faça um programa que receba 6 números inteiros em
uma lista e mostra apenas os números positivos;
'''
#Lista vazia
numeros = []
print("Informe seis números: ")
#Lista vazia recebe seis números com .append
#Primeiro faz o input de 6 números:
for cont in range(6):
	numeros.append(int(input()))
#Agora percorre a lista 'numeros' atribuindo seus valores a uma variável chamada 'numero' e mostrando se forem maiores que zero (positivos):
for numero in numeros:
	if numero > 0:
		print(numero)
