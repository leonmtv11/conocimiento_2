tupla = (5, 2, 4, 1, 3)

maximo = None
minimo = None

for numero in tupla:
    if maximo is None or numero > maximo:
        maximo = numero
    if minimo is None or numero < minimo:
        minimo = numero

print(f"El máximo valor de la tupla es: {maximo}")
print(f"El mínimo valor de la tupla es: {minimo}")
