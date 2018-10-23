'''
• Faça um programa que lê a idade de várias pessoas
(enquanto o úsuario digitar valores positivos). Em
seguida, o algoritmo deverá apresentar a quantidade 
de adolescentes (de 12 a 17 anos).
'''
adolescentes = 0
idade = 1
while idade > 0:
	idade = int(input("Digite a idade: "))
	if idade >=12 and idade <=17:
		adolescentes += 1

print("O total de adolescente é de",adolescentes)
