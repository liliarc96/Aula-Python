'''
• Cada espectador de um cinema respondeu a um
questionário no qual constava sua opinião em relação
ao filme: ótimo – 3, bom – 2, regular – 1. Faça um
programa que receba a opinião de 5 espectadores,
calcule e mostre:
• A quantidade de pessoas que responderam ótimo;
• A quantidade de pessoas que responderam bom;
• A quantidade de pessoas que responderam regular;
'''
cont = 0
otimo = 0
bom = 0
regular = 0
invalido = 0
for cont in range (0,5):
	rank = int(input("\nÓtimo – 3\nBom – 2\nRegular – 1\n"))
	if rank == 1:
		regular += 1
	elif rank == 2:
		bom += 1
	elif rank == 3:
		otimo += 1
	else:
		invalido += 1
		print("\nCÓDIGO INVÁLIDO!")
print("\nPessoas que responderam ótimo:",otimo,"\nPessoas que responderam bom:",bom,"\nPessoas que responderam regular:",regular)
print("\nVotos inválidos: ",invalido)
