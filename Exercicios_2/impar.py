'''
• Utilizando a estrutura for, faça um programa que
apresente todos os números ímpares entre 0 a 20.
'''

print("Solução 1:\n")
for numero in range (0,20):
	if numero%2 != 0:
		print(numero)

print("\n\nSolução 2:\n")
for numero in range (1,20,2):
	print(numero)
