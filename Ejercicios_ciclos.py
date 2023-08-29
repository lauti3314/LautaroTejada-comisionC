#ejercicio 1
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
cantidad = int(input("Ingrese la cantidad de lugares que recorre cada letra: "))

for i in range(5):
    frase =input(f"Ingrese la frase {i}: ").lower()
    mensaje_encriptado=""
    for letra in frase:
       posicion= letras.index(letra)
       nueva_letra= (cantidad + posicion)%27
       mensaje_encriptado = mensaje_encriptado + letras[nueva_letra] 
    print(mensaje_encriptado)

#ejercicio 2

numero = input("Ingrese el numero: ")
numero_string = str(numero)
numero = int(numero_string)

total_par=0
total_impar=0

while numero > 0:
    pares = 0
    impares = 0
    if len(numero_string) > 1:
        for i in numero_string:
            if int(i)%2 == 0:
                pares += 1
                total_par +=1
            else:
                impares +=1
                total_impar +=1
    else: 
        if numero%2 == 0:
                pares += 1
                total_par +=1
        else:
                impares +=1
                total_impar +=1
    print(f"El numero de digitos pares para el numero {numero} es de {pares} y de digitos impares es {impares}")
    numero = input("Ingrese el numero: ")
    numero_string = str(numero)
    numero = int(numero_string)
print(f"El numero total de dígitos pares es de {total_par} y de digitos impares es {total_impar}")