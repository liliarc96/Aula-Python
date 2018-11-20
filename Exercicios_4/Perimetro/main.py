'''
• Faça um programa que lê os lados de um retângulo
e calcula o seu perímetro a partir de uma função;

• Perímetro do retângulo = (2*largura) + (2*comprimento) 
'''
from funcoes import calcula_perimetro

largura = float(input("Insira a largura do retângulo: "))
comprimento = float(input("\nInsira o comprimento do retângulo: "))

resposta = calcula_perimetro(largura,comprimento)

print("\nO perímetro do retângulo é:",resposta)
