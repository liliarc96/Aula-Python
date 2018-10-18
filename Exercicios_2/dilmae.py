'''
• Faça um programa que lê a resposta de 15 usuários
para a seguinte pergunta: “Dilma será reeleita?
Digite 1 para SIM e 2 para NÃO”. Após a coleta da
resposta de cada usuário, o algoritmo deverá exibir
a quantidade de respostas para cada opção;
'''
cont = 0
sim = 0
nao = 0
invalido = 0
for cont in range (0,15):
	resposta = input('''
	Dilma será reeleita?
	Digite 1 para SIM e 2 para NÃO''')
	if resposta == "sim":
		sim += 1
	elif resposta == "nao":
		nao += 1
	else:
		invalido += 1
		print ("COMANDO INVÁLIDO!")

print("\nNúmero de votos positivos: ",sim,"\nNúmero de votos negativos: ",nao,"\nNúmero de votos inválidos: ",invalido)
