#Archivo de funciones

def most(a,b):
    if a>b:
        return a
    else : 
        return b 

def least(a,b):
    if a < b:
        return a
    else:
        return b
    
#Funciones del ahorcado

def hanged (word):

    word = word.upper()
    lives = 6
    guess_list = []
    long_word = len(word)

    for i in range(long_word):
        guess_list.append(" -- ")

    while True:

        word_guess = "".join(guess_list)

        if word_guess == word:
            print(f"Felicitaciones la palabra era {word}")
            break 
        elif lives == 0:
            return print("Ha perdido todas las vidas.")
            break

        print(f"Usted tiene {lives} vidas.")
        print(guess_list)

        letter = str(input("Ingrese una letra: ")).upper()

        if len(letter) > 1:
            print("ERROR, Debe ingresar una sola letra")
            continue

        if letter in word:
            print(f"La palabra contiene la letra {letter}")
            for y in range(long_word):
                if word[y] == letter:
                    guess_list[y] = letter
            continue
        else:
             print(f"La palabra no contiene la letra {letter}")
             lives -= 1
             continue
