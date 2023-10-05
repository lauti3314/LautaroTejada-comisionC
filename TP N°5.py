import funciones 

#1
"""
dni = input("Ingrese su DNI: ")

if funciones.verify_dni(dni) == True:
    print(f"Su DNI: {dni}, es válido.")
else:
    print("Su número de DNI es inválido.")
"""
#2
"""
phrase = str(input("Ingrese una frase: ")).lower()

print(f"La ultima palabra de su frase es {funciones.last_phrase(phrase)}")
"""
#3

print("Bienvenido \n Ingrese sus datos:")

name = input("Ingrese su primer nombre: ")
name2= input("En caso de tener otro nombre ingreselo también, sino oprima ENTER para continuar: ")
lastname= input("Ingrese su apellido: ")

while True:
  dni = input("Ingrese su número de DNI: ")

  if funciones.verify_dni(dni) == True:
    break
  else:
    print("DNI inválido, ingreselo  de nuevo correctamente. ")
    continue

print(f"Su nombre de usuario es: {name}{len(lastname)}{dni}")