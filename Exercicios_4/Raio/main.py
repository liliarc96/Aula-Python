'''
• Faça um programa que leia o raio de uma esfera e
submeta os dados para a função volume (crie a
função), que deverá calcular o seu volume;

• V = 4/3 * (R*R*R)
'''
from funcoes import volume

raio = float(input("Digite o raio da esfera: "))

resposta = volume(raio)

print("O volume da esfera é: ",resposta)
