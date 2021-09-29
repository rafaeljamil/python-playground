"""
Esta versão de pedra, papel e tesoura é jogável contra o computador. Não tem nenhuma IA
mais elaborada, apenas a bliblioteca random.
"""
import random

player_wins = 0
ai_wins = 0
draw = 0
choices = ['pedra', 'papel', 'tesoura']

while True:
    play = input("Digite pedra, papel ou tesoura. Para sair digite Q. ").lower()
    if (play == "q"):
        print("Até mais.")
        break
    if (play not in choices):
        continue
    
    rand_num = random.randint(0,2)

    ai_play = choices[rand_num]

    print("Você escolheu " + play + ".")
    print("Oponente escolheu " + ai_play + ".")

    if (play == ai_play):
        draw += 1
        print("Empate...")
    elif ((play == "pedra" and ai_play == "tesoura") or (play == "papel" and ai_play == "pedra") or (play == "tesoura" and ai_play == "papel")):
        player_wins += 1
        print("Você ganhou!")
    else:
        ai_wins += 1
        print("Você perdeu")

print("Obrigado por jogar.")
print("Você ganhou", player_wins, "vezes, empatou", draw, "vezes e perdeu", ai_wins, "vezes.")