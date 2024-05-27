def agregar_alumno():
  """Función para agregar un nuevo alumno."""
  nombre = input("Ingrese el nombre del alumno: ")
  edad = int(input("Ingrese la edad del alumno: "))
  promedio = float(input("Ingrese el promedio de calificaciones del alumno: "))

  alumno = (nombre, edad, promedio)  # Crea una tupla con la información del alumno
  alumnos.append(alumno)  # Agrega la tupla a la lista de alumnos

  print(f"Alumno {nombre} agregado correctamente.")

def ver_alumnos():
  """Función para mostrar la información de todos los alumnos."""
  if not alumnos:
    print("No hay alumnos registrados.")
  else:
    print("Listado de alumnos:")
    for alumno in alumnos:
      nombre, edad, promedio = alumno
      print(f"Nombre: {nombre}, Edad: {edad}, Promedio: {promedio:.2f}")

def buscar_alumno_por_nombre():
  """Función para buscar un alumno por su nombre."""
  nombre_buscado = input("Ingrese el nombre del alumno a buscar: ")

  alumno_encontrado = None
  for alumno in alumnos:
    nombre, _, _ = alumno
    if nombre.lower() == nombre_buscado.lower():
      alumno_encontrado = alumno
      break

  if alumno_encontrado:
    nombre, edad, promedio = alumno_encontrado
    print(f"Información del alumno {nombre_buscado}:")
    print(f"Nombre: {nombre}, Edad: {edad}, Promedio: {promedio:.2f}")
  else:
    print(f"No se encontró ningún alumno con el nombre {nombre_buscado}.")

def alumno_con_mayor_promedio():
  """Función para encontrar el alumno con mayor promedio."""
  if not alumnos:
    print("No hay alumnos registrados.")
    return

  mayor_promedio = 0
  alumno_con_mayor_promedio = None
  for alumno in alumnos:
    _, _, promedio = alumno
    if promedio > mayor_promedio:
      mayor_promedio = promedio
      alumno_con_mayor_promedio = alumno

  if alumno_con_mayor_promedio:
    nombre, edad, promedio = alumno_con_mayor_promedio
    print(f"Alumno con mayor promedio:")
    print(f"Nombre: {nombre}, Edad: {edad}, Promedio: {promedio:.2f}")
  else:
    print("No se pudo determinar el alumno con mayor promedio.")

# Inicialización de la lista de alumnos (vacía al inicio)
alumnos = []

# Menú principal
while True:
  print("Menú de Alumnos:")
  print("1. Agregar alumno")
  print("2. Ver alumnos")
  print("3. Buscar alumno por nombre")
  print("4. Alumno con mayor promedio")
  print("5. Salir")

  opcion = input("Ingrese la opción deseada (1-5): ")

  if opcion == "1":
    agregar_alumno()
  elif opcion == "2":
    ver_alumnos()
  elif opcion == "3":
    buscar_alumno_por_nombre()
  elif opcion == "4":
    alumno_con_mayor_promedio()
  elif opcion == "5":
    print("¡Gracias por usar el programa!")
    break
  else:
    print("Opción no válida. Intente nuevamente.")
