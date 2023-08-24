print("Ingrese el día y la fecha en el siguiente formato")
fecha=input("día, DD/MM: ")
partes1=fecha.split(", ")
dia=partes1[0]
partes2=partes1[1].split("/")
dd=int(partes2[0])
mm=int(partes2[1])

dia=dia.lower()

if dia=="lunes" or dia=="martes" or dia=="miercoles" or dia=="jueves" or dia=="viernes":
    if dd<1 and dd>31:
        print("La fecha ingresada es inválida")
        quit()
    elif mm==2 and dd>29:
            print("La fecha ingresada es inválida, febrero solo tiene 29 días")
            quit()
    elif mm==4 and dd>30 or mm==6 and dd>30 or mm==9 and dd>30 or mm==11 and dd>30:
            print("La fecha ingresada es inválida, el mes indicado solo tiene 30 días")
            quit()
    else:
        if dia=="lunes":
            examen=input("¿Se tomó exámen al nivel inicial?: ")
            examen=examen.lower()
            if examen=="si":
                aprobados=float(input("¿Cuantos alumnos aprobaron?: "))
                desaprobados=float(input("¿Cuantos alumnos desaprobaron?: "))
                total_alumnos=aprobados+desaprobados
                porcent_aprob=(aprobados*100)/total_alumnos
                print("Aprobó el",porcent_aprob,"% de los estudiantes")
                porcent_desaprob=(desaprobados*100)/total_alumnos
                print("Desaprobó el", porcent_desaprob, "% de los estudiantes")
                quit()
            else:
                quit()
        elif dia=="martes":
            examen=input("¿Se tomó exámen al nivel intermedio?: ")
            examen=examen.lower()
            if examen=="si":
                aprobados=float(input("¿Cuantos alumnos aprobaron?: "))
                desaprobados=float(input("¿Cuantos alumnos desaprobaron?: "))
                total_alumnos=aprobados+desaprobados
                porcent_aprob=(aprobados*100)/total_alumnos
                print("Aprobó el",porcent_aprob,"% de los estudiantes")
                porcent_desaprob=(desaprobados*100)/total_alumnos
                print("Desaprobó el", porcent_desaprob, "% de los estudiantes")
                quit()
            else:quit()
        elif dia=="miercoles":
            examen=input("¿Se tomó exámen al nivel avanzado?: ")
            examen=examen.lower()
            if examen=="si":
                aprobados=float(input("¿Cuantos alumnos aprobaron?: "))
                desaprobados=float(input("¿Cuantos alumnos desaprobaron?: "))
                total_alumnos=aprobados+desaprobados
                porcent_aprob=(aprobados*100)/total_alumnos
                print("Aprobó el",porcent_aprob,"% de los estudiantes")
                porcent_desaprob=(desaprobados*100)/total_alumnos
                print("Desaprobó el", porcent_desaprob, "% de los estudiantes")
                quit()
            else:
                quit()
        elif dia=="jueves":
            asistencia=int(input("Ingrese el porcentaje de asistencia: "))
            if asistencia>50:
                print("Asistió la mayoría")
                quit()
            else:
                print("No asistió la mayoría")
                quit()
        else:
            if dd==1 and mm==1 or dd==1 and mm==7:
                print("Comienzo de nuevo ciclo")
            nuevos=int(input("Ingrese la cantidad de nuevos alumnos: "))
            arancel=float(input("Ingrese el arancel a abonar por cada alumno: "))
            ingreso_total=nuevos*arancel
            print("Los ingresos totales serán de $", ingreso_total)
            quit()
elif dia=="sabado" or dia=="domingo":
    print("No se dictan clases los fines de semana")
    quit()
else:
    print("El día ingresado no es válido")
    quit()

