#Ejercicio 1
"""
word = input("Ingrese una palabra: ")

if len(word) == 4:
    word += "!"
else:
    word += "?"
print(word)    
"""
#Ejercicio 2
import random 
words = ["programacion", "computadora", "programa", "bucle", "javascript"]
word = random.choice(words)
max_tries = 5
tries = 0

print("Bienvenido al juego de adivinar la palabra")
print(f"Tienes {tries} intentos ")

hidden_word = "_" * len(word)

while True: 
    print(f"Palabra adivinada:", " ".join(hidden_word))
    letter = input("Ingrese una letra").lower()
    