import random

flag = True
while flag:
    bandera = True
    ran = random.randint(1,50)
    while bandera:
        try:    
            num = int(input("Guess a number between 1 and 50: \n"))
            bandera = False
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    print(ran)

    if num > 50 or num < 1:
        print("Numero fuera de rango")
    elif num == ran:
        print("Adivinaste el numero!!")
    else:
        print("Ups, perdiste")
    
    opc = input("Quieres intentarlo de nuevo? 1-Si  2-No ")
    if opc == '2':
        flag = False
