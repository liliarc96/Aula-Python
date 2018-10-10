'''
• Faça um programa que receba três notas de um aluno, calcule sua média final e diga se o mesmo
está aprovado ou reprovado (se sua média for maior que 5, está aprovado)
'''

n1 = float(input("Digite a sua primeira nota:\n"))
n2 = float(input("Digite a sua segunda nota:\n"))
n3 = float(input("Digite a sua terceira nota:\n"))

media = (n1+n2+n3)/3

if media >= 7.0:
	print("Aprovado com média",media,".")
else:
	if media > 4.0:
		print("Reprovado com média",media,".")
	else:
		print("Vai para a final com média",media,".")
