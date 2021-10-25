from Domain.rezervare import get_checkin, get_pret, creeaza_rezervare, get_all


def ieftiniri(procentaj, lista):
    """
    Functia aplica reduceri rezervarilor unde s-a facut checkin-ul
    :param procentaj: float
    :param lista: lista
    :return: lista cu reduceri aplicate(daca a fost cazul)
    """

    lista_noua = []
    for rezervare in lista:
        if get_checkin(rezervare) == "Da":
            noul_pret = get_pret(rezervare) - (procentaj / 100 * get_pret(rezervare))
            id, nume, clasa, pret, checkin = get_all(rezervare)
            rezervare_noua = creeaza_rezervare(id, nume, clasa, noul_pret, checkin)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua
