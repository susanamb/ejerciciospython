day = input("En que piensas hoy?")

words = day.split()

cont =0
for i in words:
    cont+=1
    
print(f"oh nice, me acabas de decir todo en {cont} palabras ")
