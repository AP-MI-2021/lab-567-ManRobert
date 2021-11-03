from Domain.rezervare import get_clasa
from Logic.CRUD import adauga_rezervare
from Logic.modificare_clasa import modificare_clasa


def test_modificare_clasa():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adauga_rezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = modificare_clasa("Adi", lista)
    assert get_clasa(lista[0]) == "business"
    assert get_clasa(lista[1]) == "economy plus"
    lista = modificare_clasa("Adrian", lista)
    assert get_clasa(lista[1]) == "business"
