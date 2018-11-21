'''
•Faça um programa que lê o preço de um produto
e a quantidade adquirida por um cliente. O
mesmo deverá calcular, a partir de uma função, o
valor total a ser pago pelo cliente;
'''
from funcoes import valor_total

preco = float(input("Digite o preço do produto comprado: "))
quantidade = int(input("Agora digite a quantidade comprada: "))

total = valor_total(preco,quantidade)

print("\nO valor total da compra foi de:",total)
