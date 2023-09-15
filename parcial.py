#Peticion de nombre del usuario.
name = input("Ingrese su nombre: ").title()
print(f"Hola, {name}!")

#Ciclo donde se muestran las opciones del menú, en caso no ingresar una opcion valida se reinicia el programa.
while True: 

 #Menú con opciones
 menu_options = int(input(f"{name} elija una opción \n  1-Juego de números \n  2-Juego de palabras \n  "))

 #Condicionales para las diferentes opciones elegidas.

 if menu_options == 1 :
    #Primer condicional para juego de números.
    print(f"{name} ha elegido el Juego de Números.  ")

    num_odd = 0
    counter = 0
    major_number = 0

 #Ciclo para pedir una cierta cantidad de numeros.
    while True:

        num = str(input(f"{name} ingrese un número entero (0 para terminar): "))

        #Condiciones para los numeros ingresados.
        #condicion por si no se ingresa ningún número
        if num == "":
            print("No se ingresó ningun número")
            continue
        num = float(num)
        #condición para que termine el programa
        if num == 0:
            break
        #condicion para numeros pares
        elif num % 2 == 0 and num > major_number:
            major_number = num
        #condicion para numeros impares
        elif num % 2 != 0:
            counter += 1
            num_odd += num

 #Condicionales con diferentes impresiones dependiendo los numeros ingresados
    if major_number == 0 and counter == 0:
        print("No se ingresó ningun número.")
        break
    elif major_number == 0:
        average = num_odd / counter
        print("No se ingresaron numeros pares")
        print(f"El promedio de los numeros impares es {average}.")
        break
    elif counter == 0 :
        print("No se ingresaron numeros impares")
        print(f"El mayor número par es {major_number}.")
        break
    else:
        #average sirve para sacar el promedio de los numeros impares
        average = num_odd / counter
        print(f"El mayor número par es {major_number}.")
        print(f"El promedio de los numeros impares es {average}.")
        break
    
 #Segundo condicional para juego de palabras.
 elif menu_options == 2 :

    print(f"{name} ha elegido el Juego de Palabras.")
    
    #Peticion de frase 
    sentence = str(input("Ingrese una frase: \n ")).lower()
    
    #Contador de vocales
    vowel_a = sentence.count("a")
    vowel_e = sentence.count("e")
    vowel_i = sentence.count("i")
    vowel_o = sentence.count("o")
    vowel_u = sentence.count("u")

    print(f"{name}, en la frase ingresada \n La cantidad de vocales a = {vowel_a} \n La cantidad de vocales e = {vowel_e} \n La cantidad de vocales i = {vowel_i} \n La cantidad de vocales o = {vowel_o} \n La cantidad de vocales u = {vowel_u}")
    break
 
 else:
    print("Ninguna de las opciones ingresadas es valida, elija una opción valida")