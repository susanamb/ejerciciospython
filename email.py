print("Ingresa tu correo electronico")
email = input()
email_domain = email.split('@')[1]
dom = email_domain.split('.')[0]
#print(email_domain,dom)

if dom == "gmail":
    print("Cool, tienes una cuenta de Google")
elif dom == "hotmail" or dom == "outlook":
    print("Cool, tienes una cuenta de Microsoft")
elif dom == "yahoo":
    print("Cool, tienes una cuenta de Yahoo")
else:
    print("Cool, tienes una cuenta particular de ",dom.capitalize())

