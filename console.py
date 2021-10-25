from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.determinare_pret_maxim_clasa import determinare_pret_maxim_clasa
from Logic.ieftiniri import ieftiniri
from Logic.modificare_clasa import modificare_clasa
from Logic.ordonare import ordonare


def menu():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit. ")
    print("6. Determinarea prețului maxim pentru fiecare clasă.")
    print("7. Ordonarea rezervărilor descrescător după preț. ")
    print("a. Afiseaza rezervari")
    print("x. Iesire")


def ui_adaugare(lista):
    """
    Functia citeste datele noii rezervari
    :param lista: lista
    :return: lista in urma adaugarii
    """

    id = input("Dati id-ul rezervarii ")
    nume = input("Dati numele ")
    clasa = input("Ce clasa este ? ")
    pret = float(input("Care este pretul ? "))
    checkin = input("S-a facut checkin-ul? (Da/Nu) ")
    return adauga_rezervare(id, nume, clasa, pret, checkin, lista)


def ui_stergere(lista):
    """
    Functia sterge o rezervarea cu id -ul dat
    :param lista: lista
    :return: lista in urma stergerii
    """
    id = input("Dati id-ul listei pe care doriti sa o stergeti ")
    return sterge_rezervare(id, lista)


def ui_modificare(lista):
    """
    Functia citeste id-ul rezervarii unde vor exista modificari + elementele modificate ( unde se doreste modificarea)
    :param lista: lista
    :return: lista in urma modificarii unei rezervari
    """

    id = input("Dati id-ul rezervarii pe care doriti sa o modificati ")
    nume = input("Dati noul nume ")
    clasa = input("Dati noua clasa ")
    pret = float(input("Dati noul pret "))
    checkin = input("S-a realizat checkinul?(Da/Nu) ")
    return modifica_rezervare(id, nume, clasa, pret, checkin, lista)


def show_all(lista):
    """
    Functia afiseaza toate rezervarile
    :param lista: lista
    :return: rezervarile
    """

    for rezervare in lista:
        print(to_string(rezervare))


def ui_ieftinire(lista):
    """
    Functia citeste procentajul cu care se vor reduce rezervarile la care s-a facut checkin-ul
    :param lista: lista
    :return: rezervarile in urma ieftinirilor
    """

    procentaj = float(input("Cu cat la suta vreti sa se reduca pretul rezervarilor cu checkin? "))
    return ieftiniri(procentaj, lista)


def ui_modificare_clasa(lista):
    """
    Functia citeste numele persoanei careia i se va modifica clasa intr-una superiora
    :param lista: lista
    :return: rezervarile in urma trecerii la o clasa superioara ( pentru un anume nume citit)
    """

    nume_citit = input("Care este numele persoanei/persoanelor careia/carora trebuie modificata superior clasa?"
                       "(un singur nume) ")
    return modificare_clasa(nume_citit, lista)


def ui_determinare_pret_maxim_clasa(lista):
    """
    Functia afiseaza pentru fiecare clasa pretul maxim
    :param lista: lista
    :return: None (doar afiseaza)
    """

    maxim_economy, maxim_economy_plus, maxim_business = determinare_pret_maxim_clasa(lista)
    print("Pretul maxim la clasa economy este " + str(maxim_economy))
    print("Pretul maxim la clasa economy_plus este " + str(maxim_economy_plus))
    print("Pretul maxim la clasa business este " + str(maxim_business))

    return None


def ui_ordonare(lista):
    """
    Functia returneaza rezervarile ordonate descrescator
    :param lista: lista
    :return: lista cu rezervarile ordonate descrescator
    """

    return ordonare(lista)


def meniu(lista):
    while True:
        menu()
        optiune = input("Dati optiunea ")
        if optiune == "1":
            lista = ui_adaugare(lista)
        elif optiune == "2":
            lista = ui_stergere(lista)
        elif optiune == "3":
            lista = ui_modificare(lista)
        elif optiune == "4":
            lista = ui_modificare_clasa(lista)
        elif optiune == "5":
            lista = ui_ieftinire(lista)
        elif optiune == "6":
            ui_determinare_pret_maxim_clasa(lista)
        elif optiune == "7":
            lista = ui_ordonare(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            print("La revedere ")
            break
        else:
            print("Optiune gresita, alege din nou ")

