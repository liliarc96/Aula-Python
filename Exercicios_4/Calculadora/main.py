'''
• Faça um programa que leia dois números reais e
um símbolo que identifique uma operação
matemática (+, -, *, /), submetendo-os para a
função calculadora (crie a função). A função deverá
efetuar um cálculo entre os dois números
submetidos, baseado no símbolo digitado;
'''
from funcoes import calculadora

num_1 = int(input("Digite um número real: "))
num_2 = int(input("Digite outro número real: "))
comando = input("\nDigite a operação matemática a ser usada:\n\nSoma -> +\nSubtração -> -\nMultiplicação -> *\nDivisão -> /\n")

resultado = calculadora(num_1,num_2,comando)

print("\nA resposta da operação é",resultado)
