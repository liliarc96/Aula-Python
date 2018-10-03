#Faça um algoritmo que lê o preço de um produto e a quantidade adquirida por um cliente. O mesmo deverá calcular e exibir o valor total a ser pago pelo cliente;

preco = float(input("Digite o preço:\n"))
qnt = float(input("Digite a quantidade:\n"))

total = preco * qnt

print("O valor total a ser pago é de R$",total)
