print("Bienvenide, escribe tus datos para hacer tu biografia")
flag = True
while flag:
    nombre = input("Cual es tu nombre?").lower()
    print("Cual es tu fecha de nacimiento?")
    dia = int(input("Dia: "))
    mes = int(input("Mes: (numerico, ej: enero = 1) "))
    año = int(input("Año: "))
    lugar_nac = input("Donde naciste?")
    hobbie = input("Cual es tu pasatiempo favorito?")
    print("\n------------------------------")


    if not nombre.isalpha():
        print("Ese no es un nombre valido")
    elif mes < 1 or mes > 12:
        print("Mes de nacimiento invalido")
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        print("Algo esta mal en la fecha")
    elif mes == 2 and dia > 28:
        print("ups, febrero solo tiene 28 dias")
    elif dia > 31:
        print("Revisa la fecha de nacimento, es incorrecto")
    elif año > 2021 or año < 1910:
        print("Vaya, creo que eres muy anciano para estar aqui, no creo que tengas mas de 100 años!, Corrigelo")
    else:
        print(" - Nombre: ",nombre)
        print(f" - Fecha de nacimiento: {dia} / {mes} / {año}")
        print(" - Lugar de nacimiento: ",lugar_nac)
        print(" - Tu pasatiempo es ",hobbie)
        flag = False
        break

    print("Vuelve a intentarlo")