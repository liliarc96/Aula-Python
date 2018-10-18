'''
• Faça um programa que lê diversos números
positivos e escreve o dobro de cada um. Quando
um número negativo for digitado, o algoritmo
deverá parar de ler números.
'''
multiplo = 0
numero = 0
while (numero >= 0):
	numero = int(input("Digite um número positivo:"))
	multiplo = numero * 2
	if numero >= 0:
		print("O dobro desse número é:",multiplo)
