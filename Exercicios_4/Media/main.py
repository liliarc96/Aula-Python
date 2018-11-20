'''
• Faça um programa que lê 3 notas de um aluno no
semestre, calcula sua média a partir de uma função
e informa se o aluno está aprovado (media >= 7) ou
reprovado (media < 7);
'''
from funcoes import calcula_media

print("Digite as três notas do semestre!\n")
nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
nota_3 = float(input("Terceira nota: "))

resposta = calcula_media(nota_1,nota_2,nota_3)

if resposta >= 7:
	print("\nVocê está aprovado!")
else:
	print("\nVocê está reprovado!")
