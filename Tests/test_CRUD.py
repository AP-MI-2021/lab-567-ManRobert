from Domain.rezervare import get_id, get_nume, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, get_by_id, sterge_rezervare, modifica_rezervare


def test_adauga_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    assert get_id(lista[0]) == "1"
    assert get_nume(lista[0]) == "Adi"
    assert get_by_id("1", lista) == lista[0]
    assert get_id(get_by_id("1", lista)) == "1"
    lista = adauga_rezervare("2", "Adrian", "economy plus", 200, "Da", lista)
    assert get_id(lista[1]) == "2"
    assert len(lista) == 2


def test_sterge_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adauga_rezervare("2", "Adrian", "economy plus", 200, "Da", lista)
    lista = sterge_rezervare("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_id(lista[0]) == "2"


def test_modifica_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adauga_rezervare("2", "Adrian", "economy plus", 200, "Da", lista)
    lista = modifica_rezervare("1", "Mihai", "economy", 210, "Da", lista)
    assert get_nume(get_by_id("1", lista)) == "Mihai"
    assert get_pret(get_by_id("1", lista)) == 210
    assert get_checkin(get_by_id("1", lista)) == "Da"
