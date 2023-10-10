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
"""
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
"""
#4
"""
number1 = int(input("Ingrese un número: "))
number2 = int(input("Ingrese un segundo número: "))

while True:
 if funciones.multiple(number1, number2) == True:
    print(f"{number1} es multiplo de {number2}.")
    break
 else:
   print(f"{number1} no es múltiplo de {number2}.") 
   break
"""
#5

days = int(input("Ingrese la cantidad de días que quiere calcular: "))

for i in range(days):
    maxi_tem=float(input("Ingrese la temperatura máxima(en °C sin el símbolo\"°\"): "))
    mini_tem=float(input("Ingrese la temperatura minima(en °C sin el símbolo\"°\"): "))
    media = funciones.media_calculator(maxi_tem, mini_tem)
    print(f"La temperatura media del día {i+1} fue de {media}°")

#6