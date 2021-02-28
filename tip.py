
flag = True
print("Cual es tu total a pagar?")
total = float(input())
while flag:
    per  = float(input("Que porcentaje de tip deseas dejar?\n1- 18% \n2- 20% \n3- 25%\n"))
    if per == 1:
        tip = round(total * 0.18,2)
        flag = False
        per = 18
    elif per == 2:
        tip = round(total * 0.20,2)
        flag = False
        per=20
    elif per == 3:
        tip = round(total * 0.25,2)
        flag = False
        per=25
    else:
        print("Elige una opcion valida")
        
totales = round(tip + total,2)
print(f" {per}% de tip equivale a ${tip}, haria un total de ${totales}")
