'''
• Faça um programa que repita as seguintes tarefas,
até que a palavra ‘nao’ seja digitada:
	• Leia a distância percorrida por um atleta;
	• Leia o tempo que o atleta levou para percorrer a
	distância;
	• Calcule e exiba sua velocidade média:
	• Velocidade = distancia / tempo;
	• Pergunte ao usuário se o mesmo quer continuar a
executar o programa (o usuário responderá ‘sim’ ou
‘nao’);
'''
codigo = "sim"
while codigo != "nao" and codigo == "sim":
	distancia = float(input("Digite a distância percorrida pelo atleta:"))
	tempo = float(input("\nDigite o tempo levado para percorrer a distância:"))
	
	velocidade = distancia/tempo

	print("\nA sua velocidade foi de",velocidade,"metros por segundo.")
	codigo = input("\nDeseja continuar a executar o programa?\n")

if codigo != "sim" and codigo != "nao"
	print("COMANDO INVÁLIDO!")
