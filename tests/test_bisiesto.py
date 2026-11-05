from funciones_fecha import es_bisiesto


def test_bisiesto_no():
    assert not es_bisiesto(2017)
    assert not es_bisiesto(2026)


def test_bisiesto_secular():
    assert es_bisiesto(2000)


def test_bisiesto_no_secular():
    assert es_bisiesto(1988)
    assert es_bisiesto(2016)


def test_bisiesto_secular_no():
    assert not es_bisiesto(2100)
