#Ejercicio 1
"""
x = 0

while x < 30:
    if x == 15:
        print(f'The execution of the loop was broken when x was {x}.')
        break
    elif x == 4 or x==6 or x==10:
        print(f'The value {x} of x was skipped')
        x+=1
        continue
    else :
        print(x)
    x+=1
"""
#Ejercicio 2
"""
lineas = []

while True:
    linea = input("Ingrese una línea o deje en blanco para terminar el programa: ")
    if not linea:
        break
    lineas.append(linea)
for linea in lineas:
    print(linea.upper()) 
"""
#Ejercicio 3
operacione = input('Digite la operacion con el formaro de "operacion valor", recordando que R es retirar y D depositar, deje en blanco para finalizar: ').strip(' ') #coloco el metodo strip para eliminar los espacios vacios del pricnipio y final 
operaciones = []#Para guardar las operaciones
total = 0

while operacione != '':
    operaciones.append(operacione)
    operacione = input('Digite la linea, deje en blanco para finalizar: ').strip(' ')
else:#cuando el while sea falso se ejecuto lo que esta dentro del else
    if operacione == '' and len(operaciones)==0:#Si no se ingreso desde el principio algo devuelve este mesnaje
        print('No digito ninguna operacion')
    else:#en el caso contrario recorre la lista y le hace un upper
        for i in operaciones:
            bitacora= i.split(' ')[0].upper() #divido por el espacio y selecciono el primer elemento devido al formato dado corresponde a la bitacora
            valor = int(i.split(' ')[1])# se divide por espacio y se selecciona el valor
            if bitacora == 'D':
               total+=valor
            else:
               total-=valor
        print(total)
#Ejercicio 4
numero = int(input('Digite un numero primo recuerde que un numero primo es aquel que solo se divide entre el mismo y el 1, digite cero para terminar:'))
numeros_primos = []
primo = True

while numero != 0:
    if numero == 1:
        print('Nota: Recuerda que un numero primo es mayor a 1')
        continue
    for i in range(2,numero):

        if numero%i==0 and i!=1 and i!=numero:
            primo = False
            break
        else: 
            primo= True
    if primo==True:
        numeros_primos.append(numero)
    numero = int(input('Digite un numero primo recuerde que un numero primo es aquel que solo se divide entre el mismo y el 1:'))
else:
    print(f'El numero de total de primos ingresados es de {len(numeros_primos)}')
#Ejercicio 5
age1 = input('Ingrese un primer año: ')
age2 = input('Ingrese el siguiente año: ')
for i in range(age1,age2+1):

    if i%4==0 and i%10==0 and not i%100==0:
        print(i)
    elif i%400==0:
        print(i)
    else:
        continue

#Ejercicio 6
for i in range(1,21):
       if i%2==0:
               print(i)
       else:
           continue
#Ejercicio 7 
numbers=[7,8,1,9]
num=int(input("Ingrese un número para saber si se encuentra en la lista: "))

for i in numbers:
   if num==i:
       print(f"El número {num} si se encuentra en la lista")
       break
   else:
       continue

#Ejercicio 8
print(f"¡BIENVENIDO! A continuación verá las diferentes opciones de menú\n1- Milanesa con puré\n2- Tarta de jamón y queso\n3- Ñoquis con tuco\n0- Salir")
option=1
account=0
count=[]
while option!=0:
   option=int(input("Ingrese una opción: "))
   if option==0:
       break
   elif option==1:
       print("Milanesas con pure: $1200")
       account+=1200
       count.append(1)
   elif option==2:
       print("Tarta de jamón y queso: $1400")
       account+=1400
       count.append(2)
   elif option==3:
       print("Ñoquis con tuco: $1500")
       account+=1500
       count.append(3)
   else:
       print("¡ERROR! Ingrese una opción válida")
print(f"Usted ha pedido los siguientes menús: {count}\nLa cuenta total es de ${account}")