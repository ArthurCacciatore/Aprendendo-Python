''''
Exercicio
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.
Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.


'''

A = float(input())

# Multiplica o valor por 100 para trabalhar com números inteiros
A = int(A * 100)

# Cálculo das notas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2
notas100 = A // 10000
A %= 10000
notas50 = A // 5000
A %= 5000
notas20 = A // 2000
A %= 2000
notas10 = A // 1000
A %= 1000
notas5 = A // 500
A %= 500
notas2 = A // 200
A %= 200

# Cálculo das moedas de R$ 1, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01
moedas1 = A // 100
A %= 100
moedas050 = A // 50
A %= 50
moedas025 = A // 25
A %= 25
moedas010 = A // 10
A %= 10
moedas005 = A // 5
A %= 5
moedas001 = A
