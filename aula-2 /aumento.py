#Faça um algoritmo que lê o salário de um funcionário, calcula e exibe o novo salário, sabendo que este sofreu um aumento de 25%;

salario = float(input("Digite o valor do seu salário:\n"))

salario = salario * 1.25 + salario

print("O seu salário depois do aumento é de R$",salario)
