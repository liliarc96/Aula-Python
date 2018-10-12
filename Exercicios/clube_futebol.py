'''
• Um determinado clube de futebol pretende
classificar seus atletas em categorias. Para isso, o
clube contratou você para criar um programa que
executasse essa tarefa. Baseada na tabela de
categorias do clube, construa um programa que
solicite a idade de um atleta e imprima sua
categoria;
• De 05 a 10 anos – Infantil;
• De 11 a 15 anos – Juvenil;
• De 16 a 20 anos – Júnior;
• De 21 a 25 anos – Profissional;
'''
idade = int(input("Insira a sua idade:"))

if idade >= 5 and idade <= 10:
	print("Categoria Infantil")
elif idade >= 11 and idade <= 15:
	print("Categoria Juvenil")
elif idade >= 16 and idade <= 20:
	print("Categoria Júnior")
elif idade >= 21 and idade <= 25:
	print("Categoria Profissional")
else:
	print("Categoria inexistente.")
