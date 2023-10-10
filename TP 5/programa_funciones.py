#Programa main de ejercicio de funciones

#Ejercicio funciones 1
"""
from test_funciones import most, least

x = int(input('Un número: '))
y = int(input('Otro número: '))

print(most(x-3,least(x+2, y-5)))
"""
#Ejercicio ahorcado

from test_funciones import hanged

while True:
    word = str(input("Bienvenido al ahorcado, ingrese una palabra para adivinar: "))
    
    if not word.isnumeric():
        hanged(word)
    else:
        print("Por favor, ingrese un palabra, no un número")