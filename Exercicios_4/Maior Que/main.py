'''
• Faça um programa que leia dois números inteiros e
informa, a partir de uma função, qual o maior
número digitado;
'''
from funcoes import maior_que

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite outro número inteiro: "))

resposta = maior_que(num_1,num_2)

if (resposta == num_1) or (resposta == num_2):
	print("O maior número é",resposta)
else:
	print("Os dois números são iguais.")
