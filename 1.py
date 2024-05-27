def almacenar_alumnos():
    alumnos = {}

    while True:
        nombre = input("Ingrese el nombre del alumno (o * para finalizar): ")
        if nombre == '*':
            break

        edad = int(input(f"Ingrese la edad de {nombre}: "))
        alumnos[nombre] = edad
    return alumnos


def mayor_de_edad():
    if not alumnos:
        print("No hay alumnos registrados")
        return

    mayores_de_edad = []
    for nombre,edad in alumnos.items():
        if edad >= 18:
            mayores_de_edad.append(f"{nombre} ({edad})")

    if mayores_de_edad:
        print('Alumnos Mayores de edad: ')
        for alumno in mayores_de_edad:
            print(alumno)
    else:
        print("No hay alumnos mayores de edad")


def mostrar_mayor_edad():
    if not alumnos:
        print("No hay alumnos registrados")
        return
    
    mayor_edad = max(alumnos.values())
    alumnos_mayores_de_edad = [nombre for nombre, edad in alumnos.items() if edad == mayor_edad]
    if len(alumnos_mayores_de_edad) == 1:
        print("Alumnos con mayor edad: ")
        print(f"{alumnos_mayores_de_edad[0]} ({mayor_edad})")
    else:
        print("Alumnos con mayor edad: ")
        for alumno in alumnos_mayores_de_edad:
            print(f"{alumno} ({mayor_edad})")
            

alumnos = almacenar_alumnos()
mayor_de_edad()
mostrar_mayor_edad()

        