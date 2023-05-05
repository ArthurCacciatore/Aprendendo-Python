'''
Com base na tabela abaixo, escreva um programa que leia o código de um item 
e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
CODIGO             ESPECIFICACAO            PRECO
  1                Cachorro quente          Rs 4.00
  2                   X-salada              Rs 4.50
  3                    X-Bacon              Rs 5.00
  4                 Torradas Simples        Rs 2.00
  5                   Refrigerante          Rs 1.50
 
Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''

codigo, quantidade = map(int, input().split()) 
if codigo == 1 :
    total = 4 * quantidade
elif codigo == 2 :
    total = 4.5 * quantidade
elif codigo == 3 :
    total = 5 * quantidade
elif codigo == 4 :
    total = 2 * quantidade
else :
    total = 1.5 * quantidade
print(f"Total: R$ {total:.2f}")
exit(0)