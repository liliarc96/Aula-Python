'''
• Faça um programa que leia três inteiros que
representam horas, minutos e segundos e submeta
os dados para a função converte (crie a função),
que deverá converter os três inteiros digitados para
segundos (Ex.: 2h 40min e 10s correspondem a
9.610 segundos);
'''
from funcoes import converte_segundos

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

resposta = segundos + converte_segundos(horas,minutos)

print("\nO tempo em segundos é",resposta)
