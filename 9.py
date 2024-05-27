def agregar_contacto():
  """Función para agregar un nuevo contacto."""
  nombre = input("Ingrese el nombre del contacto: ")
  telefono = input("Ingrese el número de teléfono del contacto: ")

  contacto = (nombre, telefono)  # Crea una tupla con la información del contacto
  contactos.append(contacto)  # Agrega la tupla a la lista de contactos

  print(f"Contacto {nombre} agregado correctamente.")

def buscar_contacto_por_nombre():
  """Función para buscar un contacto por su nombre."""
  nombre_buscado = input("Ingrese el nombre del contacto a buscar: ")

  contacto_encontrado = None
  for contacto in contactos:
    nombre, _ = contacto
    if nombre.lower() == nombre_buscado.lower():
      contacto_encontrado = contacto
      break

  if contacto_encontrado:
    nombre, telefono = contacto_encontrado
    print(f"Información del contacto {nombre_buscado}:")
    print(f"Nombre: {nombre}")
    print(f"Teléfono: {telefono}")
  else:
    print(f"No se encontró ningún contacto con el nombre {nombre_buscado}.")

def listar_contactos():
  """Función para mostrar la información de todos los contactos."""
  if not contactos:
    print("No hay contactos registrados.")
  else:
    print("Listado de contactos:")
    for indice, contacto in enumerate(contactos):
      nombre, telefono = contacto
      print(f"{indice+1}. {nombre}: {telefono}")

# Inicialización de la lista de contactos (vacía al inicio)
contactos = []

# Menú principal
while True:
  print("Menú de Contactos:")
  print("1. Agregar contacto")
  print("2. Buscar contacto por nombre")
  print("3. Listar contactos")
  print("4. Salir")

  opcion = input("Ingrese la opción deseada (1-4): ")

  if opcion == "1":
    agregar_contacto()
  elif opcion == "2":
    buscar_contacto_por_nombre()
  elif opcion == "3":
    listar_contactos()
  elif opcion == "4":
    print("¡Gracias por usar la libreta de contactos!")
    break
  else:
    print("Opción no válida. Intente nuevamente.")
