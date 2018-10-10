'''
• Faça um programa que receba o preço de um produto,
calcule e mostre, de acordo com as tabelas a seguir,
o novo preço e a classificação;
_____________________________________
        PREÇO        |        %      |
_____________________________________|
      Até R$ 50      |       5%      |
_____________________________________|
Entre R$ 50 e R$ 100 |       10%     |
_____________________________________|
   Acima de R$ 100   |       15%     |
_____________________________________|

_____________________________________
     NOVO PREÇO      | CLASSIFICAÇÃO |
_____________________________________|
      Até R$ 80      |    BARATO     |
_____________________________________|
Entre R$ 80 e R$ 120 |    NORMAL     |
       (inclui)      |               |
_____________________________________|
Entre R$ 120 e R$ 200|     CARO      |    
       (inclui)      |               |
_____________________________________|
   Maior que R$ 200  |  MUITO CARO   |
_____________________________________|
'''
preco = float(input("Insira o preço do produto:"))
#Aumento de preço
if (preco <= 50):
	preco = preco + preco * 0.05
elif ((preco > 50) and (preco <= 100)):
	preco = preco + preco * 0.1
else:
	preco = preco + preco * 0.15
#Fim de Aumento de preço

#Classificação
if (preco <= 80):
	print("O novo preço é %.2f e a classificação é BARATO!"% (preco))
elif ((preco > 80) and (preco <= 120)):
	print("O novo preço é %.2f e a classificação é NORMAL!"% (preco))
elif ((preco > 120) and (preco <= 200)):
	print("O novo preço é %.2f e a classificação é CARO!"% (preco))
else:
	print("O novo preço é %.2f e a classificação é MUITO CARO!"% (preco))
#Fim Classificação
