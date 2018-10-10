'''
• Faça um programa que calcula e exibe o salário
reajustado de um funcionário. O percentual de
aumento encontra-se na tabela a seguir;

         SALÁRIO              |   PERCENTUAL
   Abaixo de R$ 300,00        |      45%
Entre R$ 300,00 e R$ 600,00   |      25%
     (incluindo-os)           |
  Acima de R$ 600,00          |      15%
'''

salario = float(input("Insira o seu salário:\n"))

if(salario < 300):
	salario = (salario + (salario * 0.45))
elif(salario>=300 and salario<=600):
	salario = (salario + (salario * 0.25))
else:
	salario = (salario + (salario * 0.15))

print("O seu salário depois do aumento será de: R$ %.2f"%(salario))
