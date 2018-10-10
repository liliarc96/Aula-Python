'''
• Faça um algoritmo que lê uma sigla de um estado
brasileiro (considere que o usuário só ira digitar um dos
seguintes estados: PE, PB, SP ou RJ) e informa se o
estado digitado pertence ao Nordeste ou ao Sudeste.
'''
sigla = input("Insira o seu estado (somente PE, PB, SP ou RJ):\n")

if ((sigla == "PE" or sigla == "pe") or (sigla == "PB" or sigla == "pb")):
	print("O estado pertence a região Nordeste.")
elif ((sigla == "SP" or sigla == "sp") or (sigla == "RJ" or sigla == "rj")):
	print("O estado pertence a região Sudeste.")
else:
	print("SIGLA INCORRETA!")
