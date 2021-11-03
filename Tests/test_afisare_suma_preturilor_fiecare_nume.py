from Logic.CRUD import adauga_rezervare
from Logic.afisare_suma_preturilor_fiecare_nume import afisare_suma_preturilor_fiecare_nume


def test_afisare_suma_preturilor_fiecare_nume():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adauga_rezervare("2", "Marcel", "economy plus", 100, "Da", lista)
    lista = adauga_rezervare("3", "Marcel", "economy", 500, "Da", lista)
    lista = adauga_rezervare("4", "Ricardo", "economy", 500, "Da", lista)
    suma = afisare_suma_preturilor_fiecare_nume(lista)
    assert suma["Marcel"] == 600
    assert suma["Adi"] == 200
    assert suma["Ricardo"] == 500
