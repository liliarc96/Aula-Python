'''
• Faça um programa que receba dois números e
execute as operações listadas a seguir, de acordo com
a escolha do usuário (crie uma função para cada
opção);

CÓDIGO              OPERAÇÃO
  1      Média entre os números digitados
  2       Diferença do maior pelo menor
  3     Produto entre os números digitados
  4     Divisão do primeiro pelo segundo
'''
from funcoes import media,subtracao,multiplicacao,divisao

num_1 = float(input("\nDigite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
print("\nAgora digite o código da operação desejada:")
codigo = int(input('''\nCÓDIGO              OPERAÇÃO
  1      Média entre os números digitados
  2       Diferença do maior pelo menor
  3     Produto entre os números digitados
  4     Divisão do primeiro pelo segundo\n'''))

if codigo == 1:
	resposta = media(num_1,num_2)
elif codigo == 2:
	if num_1 >= num_2:
		resposta = subtracao(num_1,num_2)
	else:
		resposta = subtracao(num_2,num_1)
elif codigo == 3:
	resposta = multiplicacao(num_1,num_2)
elif codigo == 4:
	resposta = divisao(num_1,num_2)
else:
	print("CÓDIGO INVÁLIDO!!!")

print("A resposta da operação é",resposta)
