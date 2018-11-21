'''
• Faça um programa que leia a variação da distância
percorrida por um carro e a variação de tempo que
ele levou para percorrer o trajeto e calcula, a partir
de uma função, a velocidade média do veículo;

• Velocidade media = (Km final – km inicial) / (hora
final – hora inicial)
'''
from funcoes import velocidade_media

vel_init = float(input("Digite a velocidade inicial do veículo em km: "))
vel_end = float(input("Digite a velocidade final do veículo em km: "))
tempo_init = float(input("Digite a hora inicial do veículo em horas: "))
tempo_end = float(input("Digite a hora final do veículo em horas: "))

resposta = velocidade_media(vel_init,vel_end,tempo_init,tempo_end)

print("A velocidade do veículo é de",resposta,"kilômetros por hora.")
