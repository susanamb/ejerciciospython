
palabra= input("Escribe una palabra: ")
palabra2 = ""
for i in reversed(palabra):
    palabra2=palabra2 + i

if palabra == palabra2:
    print(palabra, " is a palindrome!")
else:
    print(palabra, " is not a palindrome")
