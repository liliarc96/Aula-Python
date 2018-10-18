'''
Exercícios
• Faça um programa que recebe o preço de 10
produtos e exibe o valor do produto mais caro;
'''
maior = 0
cont = 0
for cont in range (0,10):
	precinho = float(input("Digite o preço:"))
	if (precinho > maior):
		maior = precinho

print("O maior preço foi de:",maior)
