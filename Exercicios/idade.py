'''
• Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
• A idade desta pessoa;
• Quantos anos ela terá em 2025;
'''

nascimento = int(input("Digite o ano do seu nascimento:\n"))
ano_atual = int(input("Digite o ano atual:\n"))

idade = ano_atual - nascimento

print("Você tem",idade,"anos.\n")

idade = 2025 - nascimento

print("Você terá",idade,"anos em 2025.")
