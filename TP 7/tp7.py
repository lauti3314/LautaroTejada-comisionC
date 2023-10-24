import tp7_funciones
#1
numbers_list = []

print("Ingrese 5 numeros y luego seran ordenados:")

for i in range(5):
    number = int(input(f"Ingrese numero {i+1}: "))
    numbers_list.append(number)

sort_list = tp7_funciones.numbers_bubble_sort(numbers_list)

print(f"La lista ordenada es: {sort_list}")
#2
word_list = []

print("Ingrese una lista de palabras para ordenarla alfabeticamente: ")

for i in range(5):
    word = input(f"Palabra {i+1}: ")
    word_list.append(word)

list_word_sort = tp7_funciones.caracter_selection_sort(word_list)

print(list_word_sort)
#3

books = [
    {
        'titulo': 'El Gran Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'anio_publicacion': 1925,
    },
    {
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'anio_publicacion': 1967,
    },
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'anio_publicacion': 1949,
    },
    {
        'titulo': 'Matar un ruiseñor',
        'autor': 'Harper Lee',
        'anio_publicacion': 1960,
    },
]

field_sort = 'anio_publicacion'


books_sort = tp7_funciones.sort_books_by_field(books, field_sort)


for book in books_sort:
    print(f'Título: {book["titulo"]}, Autor: {book["autor"]}, Año de Publicación: {book["anio_publicacion"]}')

#4
word_list = []

print("Ingrese una lista de palabras para ordenarla alfabeticamente: ")

for i in range(5):
    word = input(f"Palabra {i+1}: ")
    word_list.append(word)

list_word_sort = tp7_funciones.caracter_selection_sort(word_list)

print(list_word_sort)
#5
word_list = []

print("Ingrese una lista de palabras para ordenarla alfabeticamente: ")

for i in range(5):
    word = input(f"Palabra {i+1}: ")
    word_list.append(word)

list_word_sort = tp7_funciones.caracter_selection_sort(word_list)

print(list_word_sort)
#6

numbers = [4, 2, 2, 8, 3, 3, 1]
list_sort = tp7_funciones.sort_by_count(numbers)

print("Lista original:", numbers)
print("Lista ordenada:", list_sort)

#7
print("Ingrese elementos en una lista luego sera ordenada primero por numeros y luego alfabeticamente.")

items_list = []

for i in range(5):
    element = str(input(f"Ingrese elemento {i+1}: "))
    items_list.append(element)

items_list_sort = tp7_funciones.items_list_sort(items_list)

print(f"La lista ordenada es: {items_list_sort}")
#8

numbers = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", numbers)
tp7_funciones.merge_sort(numbers)
print("Lista ordenada:", numbers)
