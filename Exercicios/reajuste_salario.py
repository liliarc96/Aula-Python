'''
• Faça um programa que calcula e exibe o salário
reajustado de um funcionário. O percentual de
aumento encontra-se na tabela a seguir;
 ___________________________________________________
 |        SALÁRIO          |       PERCENTUAL      |
 |      Até R$ 300         |          35%          |
 |    Acima de R$ 300      |          15%          |
 |_________________________________________________|
 '''

salario = float(input("Insira o valor do seu salário:\n"))

if (salario <= 300):
	salario = (salario + (salario * 0.35))
else:
	salario = (salario + (salario * 0.15))

print("O valor do salário depois do reajuste é de R$ %.2f"% (salario))
