from datetime import date, timedelta
from random import randint
from funciones_fecha import sumar_dias

DELTA_RANGE = 2500


def test_sumar_dias():
    fecha = date.today().timetuple()[:3][::-1]
    for _ in range(20):
        dias = randint(1, DELTA_RANGE)
        assert date(*sumar_dias(fecha, dias)[::-1]) == date.today() + timedelta(days=dias)


def test_restar_dias():
    fecha = date.today().timetuple()[:3][::-1]
    for _ in range(20):
        dias = randint(1, DELTA_RANGE)
        assert date(*sumar_dias(fecha, -dias)[::-1]) == date.today() - timedelta(days=dias)
    