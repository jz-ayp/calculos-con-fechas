from datetime import date, timedelta
from random import randint
from funciones_fecha import dia_anterior


def test_dia_anterior_primero():
    "Prueba la función con fechas del primer día de cada mes de un año no bisiesto"
    anho = 2026
    for mes in range(1, 13):
        assert date(*dia_anterior(1, mes, anho)[::-1]) == date(anho, mes, 1) - timedelta(days=1)

    
def test_dia_anterior_enmedio():
    "Prueba la función con días a medio mes (por simplicidad, entre el 2 y el 27)"
    anho = date.today().year
    for mes in range(1, 13):
        dia = randint(2, 27)
        assert dia_anterior(dia, mes, anho) == (dia - 1, mes, anho)
    

def test_dia_anterior_ultimo():
    "Prueba la función con el último día de cada mes del año actual"
    anho = date.today().year
    for mes in range(1, 13):
        # Ref: https://stackoverflow.com/questions/42950/get-the-last-day-of-the-month
        fecha = date(anho, mes, 28) + timedelta(days=4)
        fecha = fecha - timedelta(days=fecha.day)
        dia = fecha.day
        assert dia_anterior(dia, mes, anho) == (dia - 1, mes, anho)


def test_dia_anterior_bisiesto():
    "Prueba la función con marzo de años bisiestos"
    # Año bisiesto secular
    assert dia_anterior(1, 3, 2000) == (29, 2, 2000)
    # Año bisiesto no secular
    assert dia_anterior(1, 3, 2016) == (29, 2, 2016)
    # Año secular no bisiesto
    assert dia_anterior(1, 3, 2100) == (28, 2, 2100)
