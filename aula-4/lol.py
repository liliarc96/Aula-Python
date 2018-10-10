'''
• Faça um programa que receba dois números e
execute as operações listadas a seguir, de acordo
com a escolha do usuário;
31
CÓDIGO          OPERAÇÃO
1 ou 2    Informar o maior número
3 ou 4    Informar o menor número

Outros códigos: Relatar erro de código
'''
n1 = int(input("Digite o primeiro número:\n"))
n2 = int(input("Digite o segundo número:\n"))

codigo = int(input("\nCÓDIGO          OPERAÇÃO\n1 ou 2    Informar o maior número\n3 ou 4    Informar o menor número\n"))

if(codigo == 1 or codigo == 2):
	if(n1 > n2):
		print("O maior número é",)
