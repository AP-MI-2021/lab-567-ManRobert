from Domain.rezervare import get_pret
from Logic.CRUD import adauga_rezervare
from Logic.ieftiniri import ieftiniri


def test_ieftiniri():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adauga_rezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = ieftiniri(10, lista)
    assert get_pret(lista[1]) == 90.0
    lista = ieftiniri(10, lista)
    assert get_pret(lista[1]) == 81.0
    assert get_pret(lista[0]) == 200
