from Domain.rezervare import get_clasa, get_pret


def determinare_pret_maxim_clasa(lista):
    """
    Functia determina pretul maxim pentru fiecare clasa
    :param lista: lsita
    :return: cele 3 maxime
    """

    maxim_economy = 0
    maxim_economy_plus = 0
    maxim_business = 0

    for rezervare in lista:
        if get_clasa(rezervare) == "economy":
            if maxim_economy < get_pret(rezervare):
                maxim_economy = get_pret(rezervare)
        elif get_clasa(rezervare) == "economy plus":
            if maxim_economy_plus < get_pret(rezervare):
                maxim_economy_plus = get_pret(rezervare)
        else:
            if maxim_business < get_pret(rezervare):
                maxim_business = get_pret(rezervare)

    return maxim_economy, maxim_economy_plus, maxim_business