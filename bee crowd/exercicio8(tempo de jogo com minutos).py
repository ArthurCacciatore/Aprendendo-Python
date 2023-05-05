"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU xx HORA(S) E YYY MINUTO(S)” .
"""
hi, mi, hf, mf = map(int, input().split())
mi += (hi * 60)
mf += (hf*60)
duracao = mf - mi
if duracao <= 0  :
    duracao += 24 * 60
h = duracao // 60
min = duracao % 60
    
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format (h, min))