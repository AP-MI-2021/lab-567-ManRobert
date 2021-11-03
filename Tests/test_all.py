from Tests.test_afisare_suma_preturilor_fiecare_nume import test_afisare_suma_preturilor_fiecare_nume
from Tests.test_determinare_pret_maxim_clasa import test_determinare_pret_maxim_clasa
from Tests.test_domain import test_rezervare
from Tests.test_CRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare
from Tests.test_ieftiniri import test_ieftiniri
from Tests.test_modificare_clasa import test_modificare_clasa
from Tests.test_ordonare import test_ordonare


def test_all():
    test_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_ieftiniri()
    test_modificare_clasa()
    test_determinare_pret_maxim_clasa()
    test_ordonare()
    test_afisare_suma_preturilor_fiecare_nume()
