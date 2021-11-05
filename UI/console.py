from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.afisare_suma_preturilor_fiecare_nume import afisare_suma_preturilor_fiecare_nume
from Logic.determinare_pret_maxim_clasa import determinare_pret_maxim_clasa
from Logic.ieftiniri import ieftiniri
from Logic.modificare_clasa import modificare_clasa
from Logic.ordonare import ordonare


def menu(undo_list, redo_list):
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit. ")
    print("6. Determinarea prețului maxim pentru fiecare clasă.")
    print("7. Afisarea rezervărilor ordonate descrescător după preț. ")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume.")
    if len(undo_list) > 0:
        print("u. Undo. ")
    if len(redo_list) > 0:
        print("r. Redo ")
    print("a. Afiseaza rezervari")
    print("x. Iesire")


def ui_adaugare(lista, undo_list, redo_list):
    """
    Functia citeste datele noii rezervari
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit)
    :param undo_list: lista in care se retin rezervarile inainte de adaugare
    :param lista: lista
    :return: lista in urma adaugarii
    """
    try:
        id = input("Dati id-ul rezervarii ")
        nume = input("Dati numele ")
        clasa = input("Ce clasa este ? ")
        pret = float(input("Care este pretul ? "))
        checkin = input("S-a facut checkin-ul? (Da/Nu) ")
        rezultat = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_stergere(lista, undo_list, redo_list):
    """
    Functia sterge o rezervarea cu id -ul dat
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit)
    :param undo_list: lista in care se retin rezervarile inainte de stergere
    :param lista: lista
    :return: lista in urma stergerii
    """
    try:
        id = input("Dati id-ul rezervarii pe care doriti sa o stergeti ")
        rezultat = sterge_rezervare(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modificare(lista, undo_list, redo_list):
    """
    Functia citeste id-ul rezervarii unde vor exista modificari + elementele modificate ( unde se doreste modificarea)
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit)
    :param undo_list: lista in care se retin rezervarile inainte de modificare
    :param lista: lista
    :return: lista in urma modificarii unei rezervari
    """
    try:
        id = input("Dati id-ul rezervarii pe care doriti sa o modificati ")
        nume = input("Dati noul nume ")
        clasa = input("Dati noua clasa ")
        pret = float(input("Dati noul pret "))
        checkin = input("S-a realizat checkinul?(Da/Nu) ")
        rezultat = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    """
    Functia afiseaza toate rezervarile
    :param lista: lista
    :return: rezervarile
    """
    if len(lista) > 0:
        for rezervare in lista:
            print(to_string(rezervare))
    else:
        print("Nu exista rezervari ")


def ui_ieftinire(lista, undo_list, redo_list):
    """
    Functia citeste procentajul cu care se vor reduce rezervarile la care s-a facut checkin-ul
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit)
    :param undo_list: lista in care se retin rezervarile inainte de ieftinire
    :param lista: lista
    :return: rezervarile in urma ieftinirilor
    """
    try:
        procentaj = float(input("Cu cat la suta vreti sa se reduca pretul rezervarilor cu checkin? "))
        rezultat = ieftiniri(procentaj, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modificare_clasa(lista, undo_list, redo_list):
    """
    Functia citeste numele persoanei careia i se va modifica clasa intr-una superiora
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit)
    :param undo_list: lista in care se retin rezervarile inainte de modificare clasa
    :param lista: lista
    :return: rezervarile in urma trecerii la o clasa superioara ( pentru un anume nume citit)
    """

    nume_citit = input("Care este numele persoanei careia trebuie modificata superior clasa?"
                       "(un singur nume) ")
    rezultat = modificare_clasa(nume_citit, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_determinare_pret_maxim_clasa(lista):
    """
    Functia afiseaza pentru fiecare clasa pretul maxim
    :param lista: lista
    :return: None (doar afiseaza)
    """
    maxim_cls = determinare_pret_maxim_clasa(lista)
    for clasa in maxim_cls:
        print("Clasa {} are pretul cel mai mare de : {}".format(clasa,
                                                                maxim_cls[clasa]))
    return None


def ui_ordonare(lista):
    """
    Functia afiseaza rezervarile ordonate descrescator
    :param lista: lista
    :return: None (doar afiseaza)
    """
    lista_ordonata = []
    lista_ordonata = ordonare(lista)
    if len(lista_ordonata) > 0:
        print("Rezervarile ordonate sunt : ")
        show_all(lista_ordonata)
    else:
        print("Nu exista rezervari ")


def ui_afisare_suma_preturilor_fiecare_nume(lista):
    """
    Functia afiseaza pentru fiecare nume suma preturilor
    :param lista: lista
    :return: None (doar afiseaza)
    """

    suma = afisare_suma_preturilor_fiecare_nume(lista)
    for nume in suma:
        print("{} are suma de {}". format(nume,
                                          suma[nume]))


def meniu(lista, undo_list, redo_list):
    while True:
        menu(undo_list, redo_list)
        optiune = input("Dati optiunea ")
        if optiune == "1":
            lista = ui_adaugare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_stergere(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modificare(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_modificare_clasa(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_ieftinire(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_determinare_pret_maxim_clasa(lista)
        elif optiune == "7":
            ui_ordonare(lista)
        elif optiune == "8":
            ui_afisare_suma_preturilor_fiecare_nume(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo ")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo ")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            print("La revedere ")
            break
        else:
            print("Optiune gresita, alege din nou ")
