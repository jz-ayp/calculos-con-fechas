from datetime import date, timedelta
from random import randint
from funciones_fecha import dia_siguiente


# Generar una lista de fechas para probar la función
# Para cada mes (1-12) la lista incluye:
#  - el día primero
#  - un día al azar a medio mes (por simplicidad, entre 2 y 27)
#  - el último día del mes
def test_dia_siguiente_primero():
    "Prueba la función con fechas del primer día de cada mes del año actual"
    anho = date.today().year
    for mes in range(1, 13):
        assert dia_siguiente(1, mes, anho) == (2, mes, anho)

    
def test_dia_siguiente_enmedio():
    "Prueba la función con días a medio mes (por simplicidad, entre el 2 y el 27)"
    anho = date.today().year
    for mes in range(1, 13):
        dia = randint(2, 27)
        assert dia_siguiente(dia, mes, anho) == (dia + 1, mes, anho)
    

def test_dia_siguiente_ultimo():
    "Prueba la función con los últimos días de cada mes de un año no bisiesto"
    anho = 2026
    for mes in range(1, 13):
        # Ref: https://stackoverflow.com/questions/42950/get-the-last-day-of-the-month
        fecha = date(anho, mes, 28) + timedelta(days=4)
        fecha = fecha - timedelta(days=fecha.day)
        dia = fecha.day
        fecha_siguiente = fecha + timedelta(days=1)
        assert date(*dia_siguiente(dia, mes, anho)[::-1]) == fecha_siguiente


def test_dia_siguiente_bisiesto():
    "Prueba la función con febrero de años bisiestos"
    # Año bisiesto secular
    assert dia_siguiente(28, 2, 2000) == (29, 2, 2000)
    assert dia_siguiente(29, 2, 2000) == (1, 3, 2000)
    # Año bisiesto no secular
    assert dia_siguiente(28, 2, 2016) == (29, 2, 2016)
    assert dia_siguiente(29, 2, 2016) == (1, 3, 2016)
    # Año secular no bisiesto
    assert dia_siguiente(28, 2, 2100) == (1, 3, 2100)
