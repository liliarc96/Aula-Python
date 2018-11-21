'''
• Faça um programa que leia um número inteiro e o
submeta para a função checaPositivo (crie a
função), que deverá informar se o número digitado
é positivo ou negativo;
'''
from funcoes import checaPositivo

numero = int(input("Digite um número inteiro: "))

resposta = checaPositivo(numero)

if resposta == 1:
	print("O número é positivo!")
elif resposta == -1:
	print("O número é negativo!")
else:
	print("O número é zero!")
