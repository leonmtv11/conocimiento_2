MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

DIAS_POR_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def obtener_informacion_mes(numero_mes):

  if 1 <= numero_mes <= 12:
    return MESES[numero_mes - 1], DIAS_POR_MES[numero_mes - 1]
  else:
    return None


numero_mes = int(input("Ingrese el número del mes (1 a 12): "))

informacion_mes = obtener_informacion_mes(numero_mes)

if informacion_mes:
  nombre_mes, dias_mes = informacion_mes
  print(f"El mes {nombre_mes} tiene {dias_mes} días.")
else:
  print("Número de mes no válido.")
