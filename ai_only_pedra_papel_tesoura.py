"""
Versão de pedra, papel e tesoura jogada apenas pelo computador. Este script foi criado para visualizar
a probabilidade de ganhar, perder e empatar o jogo. Depois acabou sendo utilizado para demonstrar como
estressar o processador com cálculos. Também não tem IA complexa.
"""
import random

ai1_wins = 0
ai2_wins = 0
draw = 0
choices = ['pedra', 'papel', 'tesoura']
plays = input("Digite a quantidade de jogos: ")
if (plays.isdigit()):
    plays = int(plays)

while (plays > 0):
    
    plays -= 1

    rand_num_1 = random.randint(0,2)
    rand_num_2 = random.randint(0,2)
    # rand_num_3 = random.randint(0,2)
    # rand_num_4 = random.randint(0,2)

    # rand_num_a = int((rand_num_1 + rand_num_2) / 2)
    # rand_num_b = int((rand_num_3 + rand_num_4) / 2)

    ai1_play = choices[rand_num_1]
    ai2_play = choices[rand_num_2]

    #print("AI 1 escolheu " + ai1_play + ".")
    #print("AI 2 escolheu " + ai2_play + ".")

    if (ai1_play == ai2_play):
        draw += 1
        #print("Empate...")
    elif ((ai1_play == "pedra" and ai2_play == "tesoura") or (ai1_play == "papel" and ai2_play == "pedra") or (ai1_play == "tesoura" and ai2_play == "papel")):
        ai1_wins += 1
        #print("AI 1 ganhou!")
    else:
        ai2_wins += 1
        #print("AI 1 perdeu")

print("Resultado:")
print("AI 1 ganhou", ai1_wins, "vezes, empatou", draw, "vezes e perdeu", ai2_wins, "vezes.")