'''
• Faça um programa que repita as seguintes tarefas,
até que o código 0 seja digitado:

	•Leia o código do produto;
	•Leia a quantidade adquirida;
	•Se o código for 1, escreva 'Caderno - R$ 12.00';
	•Se for 2, escreva 'Régua - R$ 2.50';
	•Se for 3, escreva 'Borracha - R$ 0.25';
	•Se for 4, escreva 'Mochila - R$ 50.00';
	•Calcule e exiba o total a ser pago (valor * quantidade);
'''
codigo = 5
valor_total = 0.00
quantidade = 0
print('''	CÓDIGO 1 = Caderno - R$ 12.00;
	CÓDIGO 2 = Régua - R$ 2.50;
	CÓDIGO 3 = Borracha - R$ 0.25;
	CÓDIGO 4 = Mochila - R$ 50.00;

	SAIR - 0
	''')
while codigo != 0:
	codigo = int(input("\nDigite o código do produto: "))

	if codigo == 1:
		valor = 12.00
	elif codigo == 2:
		valor = 2.50
	elif codigo == 3:
		valor = 0.25
	elif codigo == 4:
		valor = 50.00
	else:
		valor = 0.00
	
	if codigo > 0 and codigo < 5:
		quantidade = int(input("\nDigite a quantidade adquirida: "))
	else:
		quantidade = 0
	
	valor_total = (valor_total + (valor * quantidade))
print("\nO valor total da compra foi de R$",valor_total)
