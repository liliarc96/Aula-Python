'''
• Faça um programa que receba dois números e
execute as operações listadas a seguir, de acordo
com a escolha do usuário;
1 - Média entre os números digitados
2 - Diferença do maior pelo menor
3 - Produto entre os números digitados
4 - Divisão do primeiro pelo segundo
'''

n1 = int(input("Digite o primeiro número:\n"))
n2 = int(input("Digite o segundo número:\n"))

codigo = int(input("\n--MENU--\n1 - Média entre os números digitados\n2 - Diferença do maior pelo menor\n3 - Produto entre os números digitados\n4 - Divisão do primeiro pelo segundo\n"))

if (codigo == 1):
	media = (n1+n2)/2
	print("A média é",media)
elif (codigo == 2):
	if (n1>=n2):
		subtracao = n1-n2
	else:
		subtracao = n2-n1
	print("A diferença do maior pelo menir número é",subtracao)
elif (codigo == 3):
	multiplicacao = n1*n2
	print("O resultado do produto dos números é",multiplicacao)
elif (codigo == 4):
	divisao = n1/n2
	print("A divisão do primeiro pelo segundo é",divisao)
else:
	print("CÓDIGO INVÁLIDO")
