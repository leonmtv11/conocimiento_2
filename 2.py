import random

# Programa principal
n = int(input("Ingrese el número de elementos: "))
rango_min = int(input("Ingrese el valor mínimo del rango: "))
rango_max = int(input("Ingrese el valor máximo del rango: "))

# Generar lista aleatoria usando random.sample
lista_aleatoria = random.sample(range(rango_min, rango_max + 1), n)

print("Lista original:")
print(lista_aleatoria)

# Ordenar la lista usando el método sort
lista_aleatoria.sort()

print("Lista ordenada:")
print(lista_aleatoria)
