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


def sumar_n_dias(fecha, dias):
    """
    Sumar una cantidad de dias a una fecha en formato dd/mm/aaaa.
    Si la cantidad de días es negativa, se trata de una resta.
    """
    if dias > 0:
        for i in range(dias):
            fecha = sumar_1_dia(fecha)
    else:
        for i in range(abs(dias)):
            fecha = restar_1_dia(fecha)
    return fecha

"""
Lo importante es la definición de arriba, lo que sigue es
sólo para probar las funciones
"""
import random
# Usaremos funciones del módulo datetime para verificar los resultados de
# las funciones que escribimos
from datetime import timedelta


# Generar números aleatorios para sumar y restar a la fecha actual y
# probar la función
fecha = date.today()
fecha = fecha.strftime('%d/%m/%Y')
for i in range(20):
    dias = random.randint(1, 2500)
    sumar = sumar_n_dias(fecha, dias)
    restar = sumar_n_dias(fecha, -dias)
    verificar_suma = date.today() + timedelta(dias)
    verificar_suma = verificar_suma.strftime('%d/%m/%Y')
    if verificar_suma == sumar:
        verificar_suma = 'Correcta'
    else:
        verificar_suma = 'Incorrecta'
    verificar_resta = date.today() - timedelta(dias)
    verificar_resta = verificar_resta.strftime('%d/%m/%Y')
    if verificar_resta == restar:
        verificar_resta = 'Correcta'
    else:
        verificar_resta = 'Incorrecta'
    print('{} + {:4d} días = {} {}'.format(fecha, dias, sumar, verificar_suma))
    print('{} - {:4d} días = {} {}'.format(fecha, dias, restar, verificar_resta))
