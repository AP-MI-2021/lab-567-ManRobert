from Logic.CRUD import adauga_rezervare
from Logic.determinare_pret_maxim_clasa import determinare_pret_maxim_clasa


def test_determinare_pret_maxim_clasa():
    lista = []
    lista = adauga_rezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adauga_rezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = adauga_rezervare("3", "Marcel", "economy", 500, "Da", lista)
    maxim_economy, maxim_economy_plus, maxim_business = determinare_pret_maxim_clasa(lista)
    assert maxim_economy == 500
    assert maxim_economy_plus == 200
    assert maxim_business == 0
