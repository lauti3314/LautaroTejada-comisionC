import test_funciones

#1
"""
dni = input("Ingrese su DNI: ")

if test_funciones.test_verify_dni(dni) == True:
    print(f"Su DNI: {dni}, es válido.")
else:
    print("Su número de DNI es inválido.")
"""
#2
"""
phrase = str(input("Ingrese una frase: ")).lower()

print(f"La ultima palabra de su frase es {test_funciones.test_last_phrase(phrase)}")
"""
#3
"""
print("Bienvenido \n Ingrese sus datos:")

name = input("Ingrese su primer nombre: ")
name2= input("En caso de tener otro nombre ingreselo también, sino oprima ENTER para continuar: ")
lastname= input("Ingrese su apellido: ")

while True:
  dni = input("Ingrese su número de DNI: ")

  if test_funciones.test_verify_dni(dni) == True:
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
 if test_funciones.test_multiple(number1, number2) == True:
    print(f"{number1} es multiplo de {number2}.")
    break
 else:
   print(f"{number1} no es múltiplo de {number2}.") 
   break
"""
#5
"""
days = int(input("Ingrese la cantidad de días que quiere calcular: "))

for i in range(days):
    maxi_tem=float(input("Ingrese la temperatura máxima(en °C sin el símbolo\"°\"): "))
    mini_tem=float(input("Ingrese la temperatura minima(en °C sin el símbolo\"°\"): "))
    media = test_funciones.test_media_calculator(maxi_tem, mini_tem)
    print(f"La temperatura media del día {i+1} fue de {media}°")
"""
#6
"""
phrase=input("Ingrese una frase: ")
print(test_funciones.test_enter_space(phrase))
"""
#7
"""
nums = test_funciones.test_fill_list()
result = test_funciones.test_number_comparator(nums)

if result:
    max_num, min_num=result
    print(f"El número máximo ingresado es: {max_num}")
    print(f"El número mínimo ingresado es: {min_num}")
else:
    print("No se ingresaron números.")
"""
#8
"""
radio=float(input("Ingrese el valor del radio de una circunferencia (en centimetros): "))
test_funciones.test_area_per_calculator(radio)
"""
#9
"""
attempt=3

while attempt>0:
    username=input("Ingrese su usuario: ")
    password=input("Ingrese la clave: ")
    if test_funciones.test_login(username,password):
        print("¡BIENVENIDO!")
        break
    else:
        attempt-=1
        print(f"Inicio de sesión fallido. Intentos restantes: {attempt}")

if attempt==0:
    print("Has agotado tus intentos")
"""
#10
"""
prices={2000:10, 4000:20, 6000:30}

print(f"El precio final de su carrito es de {test_funciones.test_aply_discount(prices)}")
"""
#11
"""
numbers=[2,6,10,43,84]

results=test_funciones.test_aply_function(test_funciones.test_multiply_by_two, numbers)

for i in range(len(numbers)):
    print(f"{numbers[i]} multiplicado por 2 es igual a {results[i]}")
"""
#12
"""
phrase=input("Ingrese una frase: ")
print(test_funciones.test_separate_phrase(phrase))
"""
#13
"""
vector = (3, 4, 5)

module = test_funciones.test_calculate_module(vector)

print("El módulo del vector es:", module)
"""
#14
"""
num=int(input("Ingrese un número: "))

if test_funciones.test_is_prime(num)==True:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
"""
#15
"""
nums=[]
test_funciones.test_list_filler(nums)

print("Factoriales de los números ingresados: ")
for num in nums:
    factorial=test_funciones.test_factorial_calculator(num)
    print(f"El factorial de {num} es {factorial}")

print(f"Se leyeron {len(nums)} números en total")
"""
#16
"""
num=int(input("Ingrese un número: "))
digit=int(input("Ingrese un digito: "))

print(f"El número {digit} se repite {test_funciones.test_frequency(num, digit)} veces en {num}")
"""
#17
"""
max_num=0

while True:
    num=int(input("Ingrese un número primo: "))
    if test_funciones.test_is_prime(num):
       if num>max_num:
           max_num=num
       
       print(f"La suma de los dígitos de {num} es {test_funciones.test_sum_of_digit(num)}")
       digit=int(input("Ingrese un dígito: "))
       print(f"El número {digit} se repite {test_funciones.test_frequency(num, digit)} veces en {num}")
    else:
        break

factorial=test_funciones.test_factorial_calculator(max_num)
print(f"El mayor número ingresado fue {max_num}")
print(f"El factorial de {max_num} es {factorial}")
"""