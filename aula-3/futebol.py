#Faça um programa que lê o número de gols marcados pelo Sport e o número de gols marcados pelo Náutico.
#Escrever o nome do time vencedor.Caso não haja vencedor, escrever EMPATE;

sport = int(input("Insira o número de gols marcados pelo Sport:\n"))
nautico = int(input("Insira o número de gols marcados pelo Náutico:\n"))

if sport == nautico:
	print("EMPATE")
elif sport > nautico:
	print("Sport venceu.")
else:
	print("Náutico venceu.")
