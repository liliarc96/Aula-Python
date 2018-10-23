'''
• Faça um programa que receba vários números
positivos (enquanto o número 0 não for digitado).
O mesmo devera exibir o maior número digitado;
'''
maior = 0
numero = 1

while numero > 0:
	numero = int(input("Digite um número: "))
	if numero >= maior:
		maior = numero

print("O maior número digitado foi",maior)
