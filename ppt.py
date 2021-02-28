import random

print("Let's play")
print("Elige: \n1-Piedra \n2-Papel \n3-Tijera")
move = int(input())
com = random.randint(1,3)
if com == 1:
    move2 = "Piedra"
elif com == 2:
    move2 = "Papel"
else:
    move2 = "Tijera"

print("Computador elige: ", move2)

if move == 1 and com == 3 or move == 2 and com == 1 or move == 3 and com == 2:
    print("GANAS!")
elif( move == com):
    print("Empate!")
else:
    print("Pierdes :( ")
