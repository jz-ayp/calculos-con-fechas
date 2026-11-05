def es_bisiesto(anho):
    "Determinar si un año dado es bisiesto"
    if anho % 400 == 0:
        bisiesto = True
    elif anho % 4 == 0 and anho % 100 != 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto


def dias_del_mes(mes, anho=None):
    "Determinar la cantidad de días que tiene un mes dado, si no se indica el año, se supone no bisiesto"
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias = 31
    elif mes in (4, 6, 9, 11):
        dias = 30
    else:
        # Febrero, necesitamos checar si el año es bisiesto
        if anho == None:
            # No se pasó el año, suponer que no es bisiesto
            dias = 28
        elif es_bisiesto(anho):
            dias = 29
        else:
            dias = 28
    return dias


def dia_siguiente(dia, mes, anho):
    "Determina la fecha del día siguiente"
    dia += 1
    if dia > dias_del_mes(mes, anho):
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anho += 1
    return (dia, mes, anho)


def dia_anterior(dia, mes, anho):
    "Determina la fecha del día anterior"
    dia -= 1
    if dia == 0:
        mes -= 1
        if mes == 0:
            mes = 12
            anho -= 1
        dia = dias_del_mes(mes, anho)
    return dia, mes, anho


def sumar_dias(fecha, dias):
    "Suma (o resta) una determinada cantidad de días a una fecha (tupla: día, mes, año)"
    dia, mes, anho = fecha
    if dias > 0:
        for i in range(dias):
            dia, mes, anho = dia_siguiente(dia, mes, anho)
    else:
        for i in range(-dias):
            dia, mes, anho = dia_anterior(dia, mes, anho)
    return dia, mes, anho

