'''
• Faça um programa que lê três números e informa qual o
maior número digitado.
'''

n1 = int(input("Insira o primeiro número:"))
n2 = int(input("Insira o segundo número:"))
n3 = int(input("Insira o terceiro número:"))

if ((n1 > n2) and (n1 > n3)):
	maior = n1
elif ((n2 > n1) and (n2 > n3)):
	maior = n2
elif ((n3 > n1) and (n3 > n2)):
	maior = n3

print("O maior número é:",maior)
