'''
• Exemplo - Faça um programa que escreve o nome
de um produto através do código digitado pelo
usuário. Se o usuário digitar 1, o programa deverá
escrever ‘Pizza’. Se o usuário digitar 2, o programa
deverá escrever ‘Hamburger’. Se o usuário digitar 3,
o programa deverá escrever ‘Refrigerante’. Se o
usuário digitar 4, o programa deverá escrever
‘Batata Frita’.
'''
codigo = int(input('''
----------MENU----------\n
CÓDIGO            COMIDA\n
  1               Pizza\n
  2             Hamburguer\n
  3            Refrigerente\n   
  4            Batata Frita\n
------------------------\n   
'''))

if codigo == 1:
	print("PIZZA!")
elif codigo == 2:
	print("HAMBURGUER!")
elif codigo == 3:
	print("REFRIGERENTE!")
elif codigo == 4:
	print("BATATA FRITA!")
else:
	print("CÓDIGO ERRADO!")
