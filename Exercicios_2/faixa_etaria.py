'''
• Faça um programa que lê a idade de várias pessoas,
até que uma idade negativa seja digitada. O
algoritmo deverá calcular e exibir a quantidade de
pessoas, de acordo com as faixas etárias
apresentadas na tabela abaixo:

FAIXA ETÁRIA           IDADE
     1ª              <= 15 anos
     2ª            Acima de 15 anos
'''
idade = 0
primeira = 0
segunda = 0
while idade >= 0:
	idade = int(input("Digite sua idade:"))
	if idade <= 15 and idade > 0:
		primeira += 1
	elif idade > 15 and idade > 0:
		segunda += 1
print("\nNúmero de pessoas na 1ª Faixa Etária:",primeira,"\nNúmero de pessoas na 2ª Faixa Etária:",segunda)
