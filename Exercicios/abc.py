'''
• Faça um programa que leia três valores inteiros A, B
e C e diga se a soma de A + B é menor que C;
'''

A = int(input("Digite o valor de A:\n"))
B = int(input("Digite o valor de B:\n"))
C = int(input("Digite o valor de C:\n"))

if ((A + B) < C):
	print("A soma de A + B é maior que C.")
elif((A + B) == C):
	print("A soma de A + B é igual a C.")
else:
	print("A soma de A + B é menor que C.")
