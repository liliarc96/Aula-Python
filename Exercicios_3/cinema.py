'''
• Cada espectador de um cinema respondeu a um
questionário no qual constava sua opinião em relação
ao filme: ótimo – 3, bom – 2, regular – 1. Faça um
programa que receba a opinião de 5 espectadores em
uma lista, calcule e mostre:
• A quantidade de pessoas que responderam ótimo;
• A quantidade de pessoas que responderam bom;
• A quantidade de pessoas que responderam regular;
'''

telespectadores = []
otimo = 0
bom = 0
regular = 0

print("Diga a dua opinião sobre o filme:\nÓtimo – 3\nBom – 2\nRegular – 1")

for i in range(5):
	telespectadores.append(int(input()))

for rank in telespectadores:
	if rank == 3:
		otimo += 1
	elif rank == 2:
		bom += 1
	elif rank == 1:
		regular += 1
print("\nA quantidade de pessoas que respondeu ótimo foi de:",otimo,"\nA quantidade de pessoas que respondeu bom foi de:",bom,"\nA quantidade de pessoas que respondeu regular foi de:",regular)
