def organizar_edades():

  edades = []

  while True:
    edad = input("Ingrese una edad (o escriba 'salir' para terminar): ")

    if edad.lower() == "salir":
      break

    try:
      edad = int(edad)
      edades.append(edad)
    except ValueError:
      print("Error: La entrada no es un número válido.")

  edades_ordenadas = sorted(edades)


  print("Edades ordenadas de menor a mayor:")
  for edad in edades_ordenadas:
    print(edad)

organizar_edades()
