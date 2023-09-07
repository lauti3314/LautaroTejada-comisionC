#Ejercicio 1
"""
word = input("Ingrese una palabra")
for i in range(10):
    print(word)
"""
#Ejercicio 2
"""
age=int(input("Ingrese su edad"))
for i in range (age):
    print(i+1)
"""
#Ejercicio 3
"""
num = int(input("Ingrese un numero: "))
impares=[]
for i in range(num):
    if i%2==0:
        impares.append(str(i+1))

impares_separados = ", ".join(impares)
print("Numeros impares: ",impares_separados)
"""
#Ejercicio 4
"""
num = int(input("Ingrese un numero: "))
count= []
for i in range(num,-1,-1):
    count.append(str(i))

countdown=", ".join(count)
print(f"La cuenta regresiva es: {countdown}")
"""
#Ejercicio 5
"""
investment=int(input("Ingrese la cantidad a invertir: "))
interest = int(input("Ingrese el porcentaje de interes anual: "))
years= int(input("Ingrese la cantidad de años: "))
aux=0

for i in range(1, years+1):
    print(f"Año: {i}")
    print(f"Capital invertido: {investment}")
    print(f"Capital + interes: {investment+interest*(interest/100)}")
    aux = aux + investment+ investment*(interest/100)
    print(f"Inversion total: {aux}")
"""
#Ejercicio 6
"""
num=int(input("ingrese un numero: "))
if num > 0: 
  for i in range(num+1):
    print("*"*i)
else :
  print("[ERROR]" "Ingrese valor positivo") 
"""
#Ejercicio 7
"""
for i in range (1, 11):
    print(f"---TABLA DEL {i}---")
    for j in range (1,11):
        product = i*j
        print(f"{i}x{j}={product}")
"""
#Ejercicio 8 
"""
num=int(input("Ingrese un número entero: "))
value=1

for i in range(1, num+1):
    row_value=value

    for j in range(i):
        print(row_value, end=" ")
        row_value-=2

    print()
    value+=2
"""
#Ejercicio 9
"""
password = ""

while password != "contraseña":
    password=input("Ingrese la contraseña: ")
    if password != "contraseña":
        print("Contraseña incorrecta, ingrese nuevamente")
print("contraseña correcta.")
"""
#Ejercicio 10
"""
num=int(input("Ingrese un número entero: "))
counter=0

for i in range(num):
    if num%(i+1)==0:
        counter=counter+1
if counter==2:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
"""
#Ejercicio 11
"""
palabra = input("Ingrese una palabra: ")

for letra in palabra[: : -1]:
 print(letra)
"""
#Ejercicio 12
phrase = str(input("Ingrese una frase: "))
letter = str(input("Ingrese una letra: "))
phrase = phrase.upper()
letter = letter.upper()

counter = 0

for character in phrase:
    if character == letter:
        counter = counter + 1
print(f"La letra \"{letter}\" se repite {counter} veces en la frase ingresada")
#Ejercicio 13
eco="eco"
while eco!="salir":
    eco=str(input("Escriba algo: "))
    print(eco)
    eco=eco.lower()
#Ejercicio 14
num1=int(input("Ingrese un número: "))    
num2=int(input("Ingrese otro número: "))

if num1<num2:
    for i in range(num1,num2+1):
        if i%2==0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")
else:
    for i in range(num2,num1+1):
        if i%2==0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")
#Ejercicio 15
num=int(input("Ingrese un número entero positivo: "))

for i in range(num):
    if num%(i+1)==0:
        print(f"{i+1} es divisor de {num}")

#Ejercicio 16
amount_num=int(input("¿Cuantos número va a ingresar?: "))

counter=0

if amount_num<0:
    print("¡ERROR! Ingrese una cantidad válida")
else:
    for i in range(amount_num):
        num=float(input("Ingrese un número: "))
        if num<0:
            counter=counter+1
print(f"Se ingresaron {counter} números negativos")

#Ejercicio 17
phrase=str(input("Escriba una frase: "))
phrase=phrase.upper()
vowels=[]

for letter in phrase:
    if letter in "AEIOU" and letter not in vowels:
        vowels.append(letter)

print(f"Las vocales en la frase son: {vowels}")

#Ejercicio 18
fibo=[0,1]

for i in range(2,10):
    next_num=fibo[i-1]+fibo[i-2]
    fibo.append(next_num)

for num in fibo:
    print(num)

#Ejercicio 19
amount=float(input("Ingrese la cantidad que desea ahorrar: $"))

if amount<0:
    print("¡ERROR! Ingrese una cantidad válida (positiva)")
else:
    saving=0

    while saving<amount:
        new_saving=float(input("Ingrese el monto que desea ingresar: $"))

        if new_saving<0:
            print("¡ERROR! Ingese una cantidad válida (positiva)")
        else:
            saving+=new_saving
            remaining=amount-saving
            print(f"Usted ha ahorrado ${saving}, le fantan {remaining} para alcanzar su objetivo de {amount}")
    
    if saving==amount:
        print(f"Usted ha alcanzado su objetivo de ahorrar ${amount}")
    else:
        additional=saving-amount
        print(f"Usted ha alcanzado su objetivo de ahorrar ${amount} y ha obtenido un adicional de {additional}")

#Ejercicio 20
num=1
addition=0
while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    if num<0:
        print("¡ERROR! Ingrese solo números enteros positivos")
    else:
        addition=addition+num
print(f"La suma de todos los números válidos ingresados es {addition}")

#Ejercicio 21
num=1
highest=0

while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    if num<0:
        print("¡ERROR! Ingrese solo números enteros positivos")
    else:
        if num>highest:
            highest=num
print(f"El mayor número ingresado fue {highest}")

#Ejercicio 22
num=0
even_number=0

while num!=-1:
    num=int(input("Ingrese un número entero positivo (o -1 para salir): "))

    if num==-1:
        break
    elif num<0:
        print("¡ERROR! Ingrese un número válido (positivo)")
    else:
        num_str=str(num)
        addition=0

        for digit_str in num_str:
            digit=int(digit_str)
            addition+=digit
        
        print(f"La suma de los dígitos de {num} es {addition}")

        if num%2==0:
            even_number+=1

print(f"Total de números pares ingresados: {even_number}")
#Ejercicio 23 y 24
product=1
total=0

while product!=0:
    product=float(input("Ingrese el valor del productor: "))
    if product<0:
        print("¡ERROR! Ingrese solo montos válidos")
    else:
        total=total+product

if total>1000:
    discount=total*0.1
    final_price=total-discount
    print(f"El total de su compra es de ${total}")
    print(f"Se le aplicó un descuento del 10%, así que el precio final es de {final_price}")
else:
    print(f"El total de su compra es de ${total}")

#Ejercicio 25
num=int(input("Ingrese un número entero positivo: "))

if num<0:
    print("¡ERROR! El número debe ser positivo")
elif num==0:
    print("El factorial de 0 es 1")
else:
    factorial=1

    for i in range(1, num+1):
        factorial*=i
    
    print(f"El factorial de {num} es {factorial}")