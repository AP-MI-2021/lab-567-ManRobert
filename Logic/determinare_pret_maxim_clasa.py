from Domain.rezervare import get_clasa, get_pret


def determinare_pret_maxim_clasa(lista):
    """
    Functia determina pretul maxim pentru fiecare clasa
    :param lista: lista
    :return: dictionar ce contine in cele 3 chei maximele
    """
    maxim_cls = {}
    for rezervare in lista:
        cls = get_clasa(rezervare)
        pretul = get_pret(rezervare)
        if cls in maxim_cls:
            if pretul > maxim_cls[cls]:
                maxim_cls[cls] = pretul
        else:
            maxim_cls[cls] = pretul
    return maxim_cls
