#1

list_numbers = []

while True:
    number= input("Ingrese un número, para finalizar ingrese 0: ")

    if number == "0":
        break
    else:
        try:
            float_num = float(number)
            list_numbers.append(float_num)
        except ValueError:
            print("Ingrese solo números.")
print(f"Sus numeros ingresados son: {list_numbers}")

#2
num_delete = int(input("Ingrese un número para eliminar de la lista: "))

if num_delete in list_numbers:
    list_numbers.remove(num_delete)
    print(f"El número {num_delete} ha sido eliminado.")
else:
    print(f"El número ingresado no se encuentra en la lista.")
    