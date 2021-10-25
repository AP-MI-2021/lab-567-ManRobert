from Domain.rezervare import get_id
from Logic.CRUD import adauga_rezervare
from Logic.ordonare import ordonare


def test_ordonare():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adauga_rezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = adauga_rezervare("3", "Marcel", "business", 210, "Nu", lista)
    lista = ordonare(lista)
    assert get_id(lista[0]) == "3"
    assert get_id(lista[1]) == "1"
    assert get_id(lista[2]) == "2"
