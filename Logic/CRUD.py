from Domain.rezervare import creeaza_rezervare, get_id


def adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    """
    Functia adauga o noua rezervare in lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista
    :return: lista cu detaliile noii rezervari din dictionar
    """

    rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def get_by_id(id, lista):
    """
    Gaseste o rezervare dupa un id primit
    :param lista : lista cu rezervari
    :return: rezervarea cu id-ul primit, sau none daca nu exista
    """

    for rezervare in lista:
        if get_id(rezervare) == id:
            return rezervare


def sterge_rezervare(id, lista):
    """
    Functia sterge rezervarea cu id-ul primit
    :param id: string
    :param lista: lista cu rezervari
    :return: lista cu rezervari fara rezervarea cu id-ul primit
    """

    return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modifica_rezervare(id, nume, clasa, pret, checkin, lista):
    """
    Functia modifica valorile cheilor pentru un anume id dat
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista
    :return: lista modificata
    """

    lista_noua = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua


