import random

# Creamos dos listas vacías para almacenar los números ganadores y los números del usuario
numbers = []
numbers2 = []

# Inicializamos un contador en 0 para llevar un registro de cuántos números coinciden
counter = 0

# Generamos una lista de 5 números aleatorios entre 1 y 99 (inclusive) como números ganadores
numbers = random.sample(range(1, 100), 5)

# Solicitamos al usuario que ingrese 5 números
for i in range(5):
    while True:
        num = input("Enter a number:")
        if not num.isdigit():
            print("Error, enter a valid number")
        else:
            num = int(num)
            # Verificamos si el número ingresado es válido (positivo y menor que 100)
            if num < 0 or num >= 100:
                print("Error, enter a valid number")
            # Verificamos si el número ya ha sido ingresado por el usuario
            elif num in numbers2:
                print("The number is already in the list")
            else:
                # Agregamos el número a la lista del usuario y salimos del bucle
                numbers2.append(num)
                break

# Comparamos los números ganadores con los números del usuario para contar las coincidencias
for i in numbers:
    for j in numbers2:
        if i == j:
            counter += 1

# Mostramos los resultados al usuario
print("The winner numbers are:", numbers)
print("The numbers in your ticket are: ", numbers2)
print(f"You hit {counter} numbers")

# Determinamos el premio en función del número de coincidencias
if counter == 5:
    print(f"You win the big lottery prize")
elif counter == 4:
    print(f"You win the 2nd lottery prize")
elif counter == 3:
    print(f"You win the 3rd lottery prize")
else:
    print("Better luck next time")
