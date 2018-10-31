'''
• LISTA
'''

numeros = [10, 20, 30]
nomes = ["José", "Maria", "Carlos"]
dados = ["alo", 2.0, 5, nomes]

idades = [int(input("Digite a primeira idade:")),int(input("Digite a segunda idade:")),int(input("Digite a terceira idade:"))]
print(idades)
#tamanho da lista
len(numeros)
#soma da lista
sum(numeros)
#maior da lista
max(numeros)
#menor da lista
min(numeros)
#.append valor ao final, .insert escolhe a posição, .pop remove o último elemento
'''   
   len(numeros)
   
=> 3
   min(numeros)
   
=> 10
   max(numeros)
   
=> 30
   numeros[0] = 888
   
   max(numeros)
   
=> 888
   sum(numeros)
   
=> 938
   numeros.insert(2,88)
   
   numeros
   
=> [888, 20, 88, 30]
   numeros.insert(0,88)
   
   numeros
   
=> [88, 888, 20, 88, 30]
'''
