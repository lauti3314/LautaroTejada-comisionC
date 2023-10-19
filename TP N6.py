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
"""
#2
num_delete = int(input("Ingrese un número para eliminar de la lista: "))

if num_delete in list_numbers:
    list_numbers.remove(num_delete)
    print(f"El número {num_delete} ha sido eliminado.")
else:
    print(f"El número ingresado no se encuentra en la lista.")

#3
added_number = sum(list_numbers)

print(f"La suamtoria de la lista da: {added_number}")
"""
#4
new_number = input("Ingrese un nuevo numero: ")
new_list=[]

try:
    float_num2 = float(new_number)
    for i in list_numbers:
        if i < float_num2:
            new_list.append(i)
            print(i)
except ValueError:
    print("Ingrese solo números.")

#5

frequencies={}

for i in list_numbers:
    frequencies[i]=frequencies.get(i, 0)+1

new_other_list=list(frequencies.items())
print(new_other_list)

#6
choice="1"
while choice=="1" or choice=="2":
    choice=input("Para agregar nombres a la lista de nivel primario oprima 1\nPara agregar nombres a la lista de nivel secundario oprima 2\nPara salir del programa oprima cualquier otra tecla: ")

    if choice=="1":
        print("NIVEL PRIMARIO")
        primary=[]

        while True:
            student=input("Ingrese un nombre de pila, oprima \"x\" para salir del programa: ").capitalize()
            if student=="X":
                break
            else:
                if not student in primary:
                    primary.append(student)

    elif choice=="2":
        print("NIVEL SECUNDARIO")
        secondary=[]
        
        while True:
            student=input("Ingrese un nombre de pila, oprima \"x\" para salir del programa: ").capitalize()
            if student=="X":
                break
            else:
                if not student in secondary:
                    secondary.append(student)
    else:
        break

print(f"NOMBRES NIVEL PRIMARIO:")
for element in primary:
    print(F"-{element}")

print(f"NOMBRES NIVEL SECUNDARIO:")
for element in secondary:
    print(F"-{element}")

repeated_names=[]
no_repeated_names=[]
for i in primary:
    for j in secondary:
        if i==j:
            repeated_names.append(i)
    if i not in secondary:
        no_repeated_names.append(i)
    

print("NOMBRES REPETIDOS ENTRE CADA NIVEL: ")
for element in repeated_names:
    print(f"-{element}")

print("NOMBRES DEL NIVEL PRIMARIO QUE NO SE REPITEN EN EL SECUNDARIO: ")
for element in no_repeated_names:
    print(f"-{element}")

#7
counter=0
string_list=[]
frequency={}

while counter<=5:
    string=input("Ingrese una letra, palabra o cadena de texto: ")
    string_list.append(string)
    counter+=1
    
for element in string_list:
    for i in element:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1

for i, frequency in frequency.items():
    print(f"\"{i}\":{frequency}")

#8
fixture=[]

for _ in range(10):
    team=[]
    for _ in range(10):
        team.append(0)
    fixture.append(team)

for i in range(10):
    for j in range(10):
        while True:
            try:
                goals=int(input(f"Ingrese la cantidad de goles que metió el Equipo {i+1} al Equipo {j+1} :"))
                fixture[i][j]=goals
                break
            except ValueError:
                print("¡ERROR! Ingrese un número válido")

triumphs=[0]*10
ties=[0]*10
defeats=[0]*10
goals_scored=[0]*10
goals_received=[0]*10

for i in range(10):
    for j in range(10):
        if i!=j:
            if fixture[i][j]>fixture[j][i]:
                triumphs[i]+=1
            elif fixture[i][j]<fixture[j][i]:
                defeats[i]+=1
            else:
                ties[i]+=1
            goals_scored[i]+=fixture[i][j]
            goals_received[i]+=fixture[j][i]

for i in range(10):
    print(f"Equipo {i+1}: ")
    print(f"Triunfos: {triumphs[i]}, Empates: {ties[i]}, Derrotas{defeats[i]}")
    print(f"Diferencia de goles: {goals_scored[i]} - {goals_received[i]}")
    print("---------")
#9
import random

rows = 4
columns = 4
board = [['||||' for _ in range(columns)] for _ in range(rows)]
revealed_board = [['  ' for _ in range(columns)] for _ in range(rows)]

def initialize_board():
    numbers = list(range(1, (rows * columns) // 2 + 1)) * 2
    random.shuffle(numbers)
    index = 0
    for i in range(rows):
        for j in range(columns):
            board[i][j] = '||||'
            revealed_board[i][j] = str(numbers[index])
            index += 1

def print_board(board_to_print):
    for i in range(rows):
        print(' '.join(board_to_print[i]))

def compare_elements(row1, column1, row2, column2):
    element1 = revealed_board[row1 - 1][column1 - 1]
    element2 = revealed_board[row2 - 1][column2 - 1]
    
    if element1 == element2:
        print("¡Coincidencia!")
        board[row1 - 1][column1 - 1] = '    '
        board[row2 - 1][column2 - 1] = '    '
        print_board(board)
    else:
        print("No coinciden.")

initialize_board()

print("Tablero inicial:")
print_board(board)

while True:
    row1 = int(input("Ingrese la fila de la primera carta: "))
    column1 = int(input("Ingrese la columna de la primera carta: "))
    print("Elemento seleccionado: " + revealed_board[row1 - 1][column1 - 1])
    
    row2 = int(input("Ingrese la fila de la segunda carta: "))
    column2 = int(input("Ingrese la columna de la segunda carta: "))
    print("Elemento seleccionado: " + revealed_board[row2 - 1][column2 - 1])
    
    compare_elements(row1, column1, row2, column2)
    
    # Verificar si todas las parejas han sido encontradas
    found_pairs = sum(row.count('    ') for row in board)
    if found_pairs == rows * columns:
        print("¡Felicidades! ¡Has encontrado todas las parejas!")
        break
    
#10
my_matriz=[]

for _ in range(3):
    rows=[]
    for _ in range(3):
        rows.append(0)
    my_matriz.append(rows)

for i in range(3):
    for j in range(3):
        while True:
            try:
                nums=float(input(f"Ingrese un número: "))
                my_matriz[i][j]=nums
                break
            except ValueError:
                print("¡ERROR! Ingrese un número válido")

print(f"DIAGONAL PRINCIPAL\n{my_matriz[0][0]}\n   {my_matriz[1][1]}\n      {my_matriz[2][2]}")
print(f"DIAGONAL INVERSA\n      {my_matriz[2][2]}\n   {my_matriz[1][1]}\n{my_matriz[0][0]}")

#11
foreign_exchange={"Euro":"€", "Dollar":"$", "Yen":"¥"}

user=input("¿El simbolo de que divisa desea conocer?: ").capitalize()
if user=="Dolar":
    user="Dollar"
    print("Quizas usted quizo escribir \"Dollar\"")

if user in foreign_exchange:
    print(f"El simbolo de {user} es {foreign_exchange[user]}")
else:
    print("La divisa que solicita no está en el diccionario")

#12
name = input("Enter your name.\n-->  ")
while True:
    age = int(input("Enter your age.\n-->  "))
    if age < 0 or age>100:
        print("Error, the age is wrong,try again.")
    else:
        break
address = input("Enter your address.\n-->  ")
cell_phone = int(input("Enter your cell phone number.\n-->  "))

profile = {'name':name,'age':age,'address':address,'cell_phone':cell_phone }
print(f"{profile['name']} tiene {profile['age']} años, vive en {profile['address']} y su número de teléfono es {profile['cell_phone']}.")

#13
fruits={}

while True:
    choice=input("Para agregar un valor oprima 1, para salir oprima cualquier tecla: ")
    
    if choice=="1":
        fruit=input("Agregue el nombre de una fruta: ").capitalize()
        while True:
            try:
                value=float(input("Ingrese el valor por kilogramo de esa fruta: $"))
                fruits[fruit]=value
                break

            except ValueError:
                print("¡ERROR! Ingrese un número válido")
    else:
        break

user=input("¿Que fruta quiere llevar?: ").capitalize()

while True:
    try:
        kg=float(input("¿Cuantos kilogramos desea llevar?. "))
        break
    except ValueError:
        print("¡ERROR! Ingrese un monto válido")

if user not in fruits:
    print("No disponemos de la fruta solicitada")

else:
    print(f"{kg}Kg de {user} sale ${fruits[user]*kg}")