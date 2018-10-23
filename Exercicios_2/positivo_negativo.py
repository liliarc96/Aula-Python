'''
• Faça um programa que lê 10 números, calcula e
exibe:
• O triplo de cada número;
• A mensagem “É positivo”, caso o número digitado seja
positivo, ou “É negativo”, caso seja negativo;
'''
cont = 1
#Em while
while (cont <= 10):
	numero = int(input("Digite um número:"))
	numero = numero*3
	print("O triplo desse número é",numero)
	if (numero >= 0):
		print("É positivo!")
	else:
		print("É negativo!")
	cont += 1

cont_2 = 0
#Em for
for cont_2 in range (0,10):
	numero = int(input("Digite um número:"))
	numero = numero*3
	print("O triplo desse número é",numero)
	if (numero >= 0):
		print("É positivo!")
	else:
		print("É negativo!")	
