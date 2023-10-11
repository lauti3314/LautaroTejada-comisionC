def verify_dni(dni):
    if len(str(dni)) == 7 or len(str(dni)) ==8:
        return True
    else:
        return False

passengers = [("Pablo", "12345678", "Mendoza"), ("Pepe", "1234567", "Mendoza"), ("Martin", "12345676", "San Juan"), ("Joaquin", "12345432", "Montevideo"), ("Marcos", "12312312", "Lima")]
citys_and_countries = [("Mendoza", "Argentina"), ("San Juan", "Argentina"), ("Montevideo", "Uruguay"), ("Lima", "Perú")]
city = ''
country = ''
name = ''
dni = 0
count = 0
while True:
    print(f"Seleccione una opcion:\n1.Agregar pasajeros a la lista de viajeros\n2.Agregar ciudades a la lista de ciudades\n3.Buscar a que ciudad viaja por DNI\n4.Mostrar cantidad de pasajeros que viajan a una ciudad\n5.Buscar pais al que viaja por DNI\n6.Mostrar cuantos pasajeros viajan a un pais\n0. Salir")
    option = int(input())
    if option == 1:
        while True:
            print(f"Ingrese los siguientes datos:\n")
            name = input("Nombre:")
            dni = int(input("DNI:"))
            city = input("Ciudad:")
            if verify_dni(dni) == True:
                passengers.append((name, dni, city))
                break
            else: 
                print("Ingrese un dni valido por favor")
    elif option == 2:
        city = input("Ingrese el nombre de la ciudad: ")
        country = input("Ingrese en pais al que pertenece la ciudad: ")
        citys_and_countries.append((city, country))
    elif option == 3:
        print(f"Ingrese el DNI del pasajero:")
        dni = int(input("DNI:"))
        for person in passengers:
            if person[1] == dni:
                print(f"La ciudad a la que viaja el pasajero con el dni {dni} es {person[2]}")

    elif option == 4:
        city = input("Ingrese una ciudad: ")
        for person in passengers:
            if person[2] == city:
                count += 1
        print(f"La cantidad de pasajeros que viajan a {city} es de {count}")
    elif option == 5:
        dni = int(input("Ingrese DNI:"))
        for person in passengers:
            for location in citys_and_countries:
                if person[1] == dni:
                    if person[2] == location[0] :
                        print(f"El pais al que pertenece es {location[1]}")
                    else:
                        print(f"No se ha podido encontrar el pais al cual pertenece {person[2]}")
    elif option == 6:
        country = input("Ingrese un pais:")
        for person in passengers:
            for location in citys_and_countries:
                if person[2] == location[0] and location[1] == country:
                    count += 1
        print(f"La cantidad de personas que viajan a {country} es de {count}")
    elif option == 7:
        print("Adios :)")
        break
