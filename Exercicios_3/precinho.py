'''
• Faça um programa que receba o preço de cinco
produtos em uma lista, calcula e exiba:
• A quantidade de produtos com preço inferior a R$ 50,00;
• A quantidade de produtos com preço entre R$ 50,00 e
80,00;
• A quantidade de produtos com preço acima de R$ 80,00
• A média de preço dos produtos;
'''
inferior = 0
entre = 0
superior = 0
precinho = []

print("Digite o preço de cinco produtos!\n")

for i in range(5):
	precinho.append(float(input()))

for preco_produto in precinho:
	if preco_produto < 50:
		inferior += 1
	elif preco_produto >= 50 and preco_produto <= 80:
		entre += 1
	else:
		superior += 1

media = sum(precinho)/len(precinho)
#ou media = sum(precinho)/5

print("\nA quantidade de produtos com preço inferior a R$ 50,00 é de:",inferior)
print("\nA quantidade de produtos com preço entre R$ 50,00 e 80,00 é de:",entre)
print("\nA quantidade de produtos com preço acima de R$ 80,00 é de:",superior)
print("\nA média de preço dos produtos é de:",media)
