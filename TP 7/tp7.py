import tp7_funciones
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

#5
#6

numbers = [4, 2, 2, 8, 3, 3, 1]
list_sort = tp7_funciones.sort_by_count(numbers)

print("Lista original:", numbers)
print("Lista ordenada:", list_sort)

#7
#8

numbers = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", numbers)
tp7_funciones.merge_sort(numbers)
print("Lista ordenada:", numbers)
