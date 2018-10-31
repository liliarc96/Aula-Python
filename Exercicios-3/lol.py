'''
• Faça um programa que lê o sexo de 3 pessoas em
uma lista, calcula e exibe a quantidade de pessoas
de cada sexo;
'''
pessoa = []
mulheres = 0
homens = 0

print("Digite o sexo de três pessoas: ")

for cont in range(3):
	pessoa.append(string(input()))

for sexo in pessoa:
	if sexo == "feminino"
		mulheres += 1
	elif sexo == "masculino"
		homens += 1

print("O número de mulheres é de", mulheres, "e de homens é", homens)
