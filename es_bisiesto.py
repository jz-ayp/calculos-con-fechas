def es_bisiesto(anho):
    "Determinar si un año es bisiesto."
    if anho % 400 == 0:
        bisiesto = True
    elif anho % 100 != 0 and anho % 4 == 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto

"""
Lo importante es la definición de arriba, lo que sigue es sólo para probar
la función.
"""
anho = eval(input('Introduzca un año: '))
if es_bisiesto(anho):
    print('El año sí es bisiesto')
else:
    print('El año no es bisiesto')
