#ejercicio 1
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
cantidad = int(input("Ingrese la cantidad de lugares que recorre cada letra: "))

for i in range(6):
    frase =input(f"Ingrese la frase {i}: ").lower()
    mensaje_encriptado=""
    for letra in frase:
       posicion= letras.index(letra)
       nueva_letra= (cantidad + posicion)%27
       mensaje_encriptado = mensaje_encriptado + letras[nueva_letra] 
    print(mensaje_encriptado)

#ejercicio 2
