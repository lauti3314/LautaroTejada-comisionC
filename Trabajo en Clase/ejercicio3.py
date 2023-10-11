import datetime

def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def get_membership_number():
    while True:
        try:
            membership_number = int(input("Ingrese el número de socio: "))
            if any(member["member"] == membership_number for member in members):
                print("¡Error! El número de socio ya está en uso. Intente con otro número.")
            else:
                return membership_number
        except ValueError:
            print("¡Error! Por favor, ingrese un número válido.")

def get_date():
    while True:
        new_date = input("Ingrese la fecha de ingreso (dd/mm/yyyy): ")
        if validate_date(new_date):
            return new_date
        else:
            print("¡Error! Por favor, ingrese una fecha válida en formato dd/mm/yyyy.")

members = [
    {"member": 1, "name": "Amanda Núñez", "start_date": "17/03/2009", "fee": True},
    {"member": 2, "name": "Bárbara Molina", "start_date": "17/03/2009", "fee": True},
    {"member": 3, "name": "Lautaro Campos", "start_date": "17/03/2009", "fee": True}
]

while True:
    print("1. Mostrar cantidad de socios")
    print("2. Registrar pago por número de socio")
    print("3. Modificar fecha de ingreso")
    print("4. Dar de baja por número de socio")
    print("5. Mostrar todos los socios")
    print("6. Registrar un nuevo socio")
    print("0. Salir")
    option = input("Ingrese una opción: ")

    if option == "1":
        print(f"Cantidad de socios: {len(members)}")
    elif option == "2":
        membership_number = int(input("Ingrese el número de socio para registrar el pago: "))
        for member in members:
            if member["member"] == membership_number:
                member["fee"] = True
                print("Pago registrado exitosamente.")
                break
        else:
            print("Socio no encontrado.")
    elif option == "3":
        print("Ingrese la fecha que desea reemplazar:")
        old_date = get_date()
        print("Ingrese la nueva fecha:")
        new_date = get_date()
        modification_count = 0
        for member in members:
            if member["start_date"] == old_date:
                member["start_date"] = new_date
                modification_count += 1
        print(f"Se modificaron las fechas de ingreso de {modification_count} socios.")
    elif option == "4":
        try:
            membership_number = int(input("Ingrese el número de socio a dar de baja: "))
            for member in members:
                if member["member"] == membership_number:
                    members.remove(member)
                    print(f"Socio {membership_number} dado de baja exitosamente.")
                    break
            else:
                print("Socio no encontrado.")
        except ValueError:
            print("¡Error! Por favor, ingrese un número válido para el socio.")
    elif option == "5":
        for member in members:
            print(f"Socio {member['member']}: {member['name']} - Fecha de ingreso: {member['start_date']} - Cuota al día: {member['fee']}")
    elif option == "6":
        new_membership_number = get_membership_number()
        new_name = input("Ingrese el nombre y apellido del nuevo socio: ")
        new_start_date = get_date()
        new_member = {
            "member": new_membership_number,
            "name": new_name,
            "start_date": new_start_date,
            "fee": True
        }
        members.append(new_member)
        print("Nuevo socio registrado exitosamente.")
    elif option == "0":
        print("Adiós :)")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
