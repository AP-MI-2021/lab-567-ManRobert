from Domain.rezervare import get_id
from Logic.CRUD import adauga_rezervare
from Logic.ieftiniri import ieftiniri
from Logic.modificare_clasa import modificare_clasa


def test_undo_redo_console():
    # Simularea scenariului primit de teste
    # Nu este necesar sa testam si (undo, redo) in command_line


    # lista , undo_lista, redo_lista sunt goale la inceput
    lista = []
    undo_list = []
    redo_list = []


    # In cazul primelor simulari de adaugare nu e necesar sa scriem redo_list.append(lista)
    # Pentru ca ca nu s-a facut undo, redo fiind indisponibil


    # se adauga prima rezervare
    rezultat = adauga_rezervare("1", "Marcel", "business", 200, "Da", lista)
    undo_list.append(lista)
    lista = rezultat


    # se adauga a 2 a rezervare
    rezultat = adauga_rezervare("2", "Marcel2", "business", 2000, "Da", lista)
    undo_list.append(lista)
    lista = rezultat


    # se adauga a 3 a rezervare
    rezultat = adauga_rezervare("3", "Marcel3", "business", 20, "Da", lista)
    undo_list.append(lista)
    lista = rezultat


    # assert pentru cele 3 obiecte adaugate
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "2"
    assert get_id(lista[2]) == "3"


    # se face undo + assert
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_id(lista[1]) == "2"
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]


    # se face inca un undo + assert
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert undo_list == [[]]


    # se face inca un undo + assert
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert undo_list == []
    assert get_id(redo_list[2][0]) == "1"


    # se face inca un undo + assert (fara efect)
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list
    assert len(lista) == 0
    assert undo_list == []
    assert get_id(redo_list[2][0]) == "1"


    # se adauga 3 rezervari + assert
    rezultat = adauga_rezervare("1", "Marcel", "business", 200, "Da", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    rezultat = adauga_rezervare("2", "Marcel3", "business", 2000, "Da", lista)
    undo_list.append(lista)
    lista = rezultat

    rezultat = adauga_rezervare("3", "Marcel3", "business", 20, "Da", lista)
    undo_list.append(lista)
    lista = rezultat

    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3


    # se face redo (fara efect)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3


    # se fac 2 undo-uri + assert-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_id(lista[1]) == "2"
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert undo_list == [[]]


    # se face redo + assert
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert len(lista) == 2


    # se face redo + assert
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # se fac 2 undo-uri + assert-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_id(lista[1]) == "2"
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert undo_list == [[]]


    # se adauga rezervarea cu id ul 4
    rezultat = adauga_rezervare("4", "Marcel4", "economy", 200, "Da", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()


    # se face redo (fara efect)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(undo_list) == 2
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]


    # se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert len(undo_list) == 1
    assert len(redo_list) == 1


    # se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert len(undo_list) == 0
    assert len(redo_list) == 2


    # se face 2 redo-uri
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 1

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0


    #se face ultimul redo
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0
    assert len(undo_list) == 2


    # Teste cu assert și pentru operațiunile care modifică mai multe entități
    #test modificare clasa superioara
    nume = "Marcel4"
    undo_list.append(lista)
    redo_list.clear()

    lista = modificare_clasa(nume, lista)
    assert lista[1][2] == "economy plus"

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][2] == "economy"

    undo_list.append(lista)
    lista = redo_list.pop()
    assert lista[1][2] == "economy plus"

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][2] == "economy"


    # test ieftinire + undo + assert-uri
    procentaj = 100
    undo_list.append(lista)
    redo_list.clear()

    lista = ieftiniri(procentaj, lista)
    assert lista[1][3] == 0

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][3] == 200

    undo_list.append(lista)
    lista = redo_list.pop()
    assert lista[1][3] == 0

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][3] == 200









