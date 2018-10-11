'''
• Exemplo: Faça um programa que sempre recebe
números inteiros e conta quantos números foram
iguais a 2. Caso o usuário digite o número 0, o
programa deverá parar de receber valores e exibir
quantos números foram iguais a 2;
'''
numero = 1
contador = 0

while numero != 0:
	numero = int(input("Digite um número:"))
	if numero == 2:
		contador = contador + 1
print("O número 2 foi digitado %i vezes." %(numero))

#pyformat.info
