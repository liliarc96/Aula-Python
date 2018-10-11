'''
• Exemplo: Faça um programa que sempre repetirá a
frase ‘Você não sabe a senha! =P’ enquanto o
usuário não digitar a senha ‘naodigo’;
'''

senha = input("Descubra a senha:\n")

while senha != "naodigo":
	print("Você não sabe a senha! =P")
	senha = input("Descubra a senha:\n")
print("Você sabe a senha!")
