'''
• Faça um programa que leia o código de origem de
um produto e mostre sua procedência. A
procedência obedece a tabela a seguir:

Código de Origem     Procedência
   1 ou 2                Sul
   3 ou 4              Sudeste
   5 ou 6               Norte
   7 ou 8             Nordeste
  9 ou 10           Centro-Oeste
'''

codigo = int(input("Digite o código do produto:\n"))

if(codigo == 1 or codigo == 2):
	print("O produto vem da região Sul.")
elif(codigo == 3 or codigo == 4):
	print("O produto vem da região Sudeste.")
elif(codigo == 5 or codigo == 6):
	print("O produto vem da região Norte.")
elif(codigo == 7 or codigo == 8):
	print("O produto vem da região Nordeste.")
elif(codigo == 9 or codigo == 10):
	print("O produto vem da região Centro-Oeste.")
else:
	print("CÓDIGO INCORRETO!")
