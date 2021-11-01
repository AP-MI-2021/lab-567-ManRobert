from Domain.rezervare import get_nume, get_clasa, to_string, get_all, creeaza_rezervare


def modificare_clasa(nume_citit, lista):
    """
    Functia trece toate rezervarile la o clasa superioara pentru un nume citit
    :param nume_citit: string
    :param lista: lista
    :return: lista rezervarilor cu modificarea claselor (daca a fost cazul)
    """

    lista_noua = []
    for rezervare in lista:
        if get_nume(rezervare) == nume_citit:
            if get_clasa(rezervare) == "economy":
                noua_clasa = "economy plus"
            elif get_clasa(rezervare) == "economy plus":
                noua_clasa = "business"
            else:
                print("Rezervarea " + to_string(rezervare) + ", este deja la cea mai superioara clasa ")
                noua_clasa = get_clasa(rezervare)

            id, nume, clasa, pret, checkin = get_all(rezervare)
            rezervare_cls_modificata = creeaza_rezervare(id, nume, noua_clasa, pret, checkin)
            lista_noua.append(rezervare_cls_modificata)
        else:
            lista_noua.append(rezervare)

    return lista_noua
