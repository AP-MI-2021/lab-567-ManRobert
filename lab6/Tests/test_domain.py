from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin, get_all


def test_rezervare():
    rezervare = creeaza_rezervare("1", "Marcel", "business", 1000, "Da")
    assert get_id(rezervare) == "1"
    assert get_nume(rezervare) == "Marcel"
    assert get_clasa(rezervare) == "business"
    assert get_pret(rezervare) == 1000
    assert get_checkin(rezervare) == "Da"
    assert get_all(rezervare) == ("1", "Marcel", "business", 1000, "Da")

    id, nume, clasa, pret, checkin = get_all(rezervare)
    assert id == "1"
    assert clasa == "business"
    assert checkin == "Da"
