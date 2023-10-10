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

#Funciones TP N°5

#1.	
def test_verify_dni (dni):
    if len(dni) == 7 or len(dni)==8:
        return True
    else:
        return False
    
#2.
def test_last_phrase (phrase):
    words = phrase.split() [-1]
    return words

#4
def test_multiple (number1, number2):
    if number1 % number2 == 0 :
        return True
    else:
        return False

#5
def test_media_calculator(maxi,mini):
    media=(maxi+mini)/2
    return media

#6
def test_enter_space (phrase):
    new_phrase=""
    for letter in phrase:
        new_phrase+=letter + " "
    return new_phrase

#7
def test_fill_list():
    nums=[]
    n=int(input("Ingrese la cantidad de números que desea ingresar: "))
    for i in range(n):
        num=float(input("Ingrese un número: "))
        nums.append(num)
    return nums

def test_number_comparator(nums):
    if not nums:
        return None
    
    max_num=min_num=nums[0]
    for num in nums:
        if num>max_num:
            max_num=num
        elif num<min_num:
            min_num=num
    return max_num, min_num
#8
import math
def test_area_per_calculator(radio):
    perimeter=radio*2
    area=math.pi*(radio)**2
    return(print(f"El perímetro de la circunferencia es de {perimeter} cm y el area es de {area} cm2"))
#9
def test_login (username, password):
    
    if username=="usuario1" and password=="asdasd":
        return True
    else:
        return False
#10
def test_aply_discount(prices):
    final_price=0
    shopping_cart=float(input("Ingrese el monto total de su carrito de compra: "))
    if shopping_cart<=0:
        print("¡ERROR! El valor ingresado no es válido")
        test_aply_discount(prices)
    else:    
        if shopping_cart>=2000 and shopping_cart<4000:
            discount=(shopping_cart*prices[2000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[2000]}%")

        elif shopping_cart>=4000 and shopping_cart<6000:
            discount=(shopping_cart*prices[4000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[4000]}%")

        elif shopping_cart>=6000:
            discount=(shopping_cart*prices[6000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[6000]}%")

        else:
            final_price=shopping_cart
            print(f"Por el monto de su carrito no obtiene ningún descuento")

        return final_price
#11

#12

#13

#14

#15

#16

#17
