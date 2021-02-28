print("Odd or even")

flag= True

while flag:
    num = int(input("What number are you thinking? "))

    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")

    opc = int(input("\n Quiere continuar? \n 1-Si \n 2-No \n"))
    if opc != 1:
        flag = False
