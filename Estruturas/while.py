'''
• Faça um programa que simule uma urna
eletrônica e receba números inteiros. O programa 
irá contar quantos números foram iguais a 17 e 
quantos foram iguais a 13. Caso o usuário digite o 
número 0, o programa deverá parar de receber 
valores e exibir o resultado da quantidade de 
números.
'''
voto_b, voto_h = 0, 0
voto = 1

while voto != 0:
	voto = int(input("\nDigite o número do candidato: "))
	if voto == 13:
		voto_h += 1
	elif voto == 17:
		voto_b += 1
	else:
		print("Voto inválido.")
print("\nNúmero de pessoas que votaram 13:",voto_h, "\nNúmero de pessoas que votaram 17:",voto_b)
#print("Número de pessoas que votaram 13: %d\n Número de pessoas que votaram 17: %d\n" %(voto_h, voto_b))
#print("Número de pessoas que votaram 13: {}\n Número de pessoas que votaram 17: {}".format(voto_h,voto_b))
#pyformat
