from Domain.rezervare import get_nume, get_pret


def afisare_suma_preturilor_fiecare_nume(lista):
    """
    Functia calculeaza suma preturilor pentru fiecare nume
    :param lista: lista
    :return: dictionar ce contine ca si cheie pentru fiecare nume suma calculata
    """

    suma = {}
    for rezervare in lista:
        numele = get_nume(rezervare)
        pretul = get_pret(rezervare)
        if numele in suma:
            suma[numele] = suma[numele] + pretul
        else:
            suma[numele] = pretul
    return suma