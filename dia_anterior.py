from datetime import date


def es_bisiesto(anho):
    "Determinar si un año es bisiesto."
    if anho % 400 == 0:
        bisiesto = True
    elif anho % 100 != 0 and anho % 4 == 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto


def dias_del_mes(mes, anho=None):
    "Cantidad de días que tiene el mes."
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    elif mes in [4, 6, 9, 11]:
        dias = 30
    elif mes == 2:
        # Necesitamos checar si es bisiesto
        if anho is None:
            # No se pasó el año, tomar el actual
            anho = date.today().year
        if es_bisiesto(anho):
            dias = 29
        else:
            dias = 28
    return dias


def sumar_1_dia(fecha):
    "Sumar un día a una fecha en formato dd/mm/aaaa."
    # Extraer los elementos de la fecha.
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    anho = int(fecha[6:])
    # Sumar 1 al día
    dia += 1
    # Checar que no nos pasamos
    if dia > dias_del_mes(mes, anho):
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anho += 1
    fecha = '{:02d}/{:02d}/{:04d}'.format(dia, mes, anho)
    return fecha


def restar_1_dia(fecha):
    "Restar un día a una fecha en formato dd/mm/aaaa."
    # Extraer los elementos de la fecha.
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    anho = int(fecha[6:])
    # Restar 1 al día
    dia -= 1
    # Checar que no nos pasamos
    if dia < 1:
        mes -= 1
        if mes < 1:
            mes = 12
            anho -= 1
        dia = dias_del_mes(mes, anho)
    fecha = '{:02d}/{:02d}/{:04d}'.format(dia, mes, anho)
    return fecha


"""
Lo importante es la definición de arriba, lo que sigue es
sólo para probar las funciones
"""
# Usaremos el módulo random para generar días al azar
# La función random.randint genera enteros al azar entre un rango
# curiosamente (para Python) los números generados incluyen también
# el límite superior.
import random

# Generar una lista de fechas para probar la función
# Para cada mes (1-12) la lista incluye:
#  - el día primero
#  - un día al azar a medio mes (por simplicidad, entre 2 y 27)
#  - el último día del mes
fechas = []
anho = date.today().year
for mes in range(1, 13):
    # Primer día del mes
    fechas.append('{:02d}/{:02d}/{:04d}'.format(1, mes, anho))
    # Día a medio mes
    dia = random.randint(2, 27)
    fechas.append('{:02d}/{:02d}/{:04d}'.format(dia, mes, anho))
    # Último día del mes
    dia = dias_del_mes(mes, anho)
    fechas.append('{:02d}/{:02d}/{:04d}'.format(dia, mes, anho))
# Agregar a la lista casos especiales para los años bisiestos
# Año bisiesto secular
fechas.append('28/02/2000')
fechas.append('29/02/2000')
fechas.append('01/03/2000')
# Año bisiesto no secular
fechas.append('28/02/2016')
fechas.append('29/02/2016')
fechas.append('01/03/2016')
# Año secular no bisiesto
fechas.append('28/02/2100')
fechas.append('01/03/2100')
# Año no secular y no bisiesto
fechas.append('28/02/2017')
fechas.append('01/03/2017')

# Probar la función con la lista de fechas
print('Calcular las fechas de los días anterior y siguiente')
for fecha in fechas:
    siguiente = sumar_1_dia(fecha)
    anterior = restar_1_dia(fecha)
    print(anterior, '<', fecha, '>', siguiente)
