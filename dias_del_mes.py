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


"""
Lo importante son las definiciones de arriba, lo que sigue es sólo para
probar la función.
"""
print('Calcular los días que tiene un mes')
mes = eval(input('Introduzca el número de mes: '))
anho = input('Introduzca un año (Enter para ninguno): ')
if anho.strip() == '':
    # No se introdujo el anho
    dias = dias_del_mes(mes)
else:
    dias = dias_del_mes(mes, eval(anho))
print('El mes tiene {} días'.format(dias))
