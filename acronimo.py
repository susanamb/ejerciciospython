print("Escribe algo:")
word = input()

word = word.split()
acron = ""

for i in word:
    acron=acron+i[0]

acron = acron.upper()
print(acron)