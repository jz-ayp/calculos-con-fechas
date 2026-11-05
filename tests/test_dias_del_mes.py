from funciones_fecha import dias_del_mes


DIAS_DEL_MES = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10:31,
    11: 30,
    12: 31
}


def test_dias_del_mes_sin_anho():
    for mes in range(1, 13):
        assert dias_del_mes(mes) == DIAS_DEL_MES[mes]


def test_dias_del_mes_no_bisiesto():
    for mes in range(1, 13):
        assert dias_del_mes(mes, 2025) == DIAS_DEL_MES[mes]
        assert dias_del_mes(mes, 2026) == DIAS_DEL_MES[mes]

def test_dias_del_mes_bisiesto():
    for mes in (x for x in range(1, 13) if x != 2):
        assert dias_del_mes(mes, 2024) == DIAS_DEL_MES[mes]
    assert dias_del_mes(2, 2024) == 29
