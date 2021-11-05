from copy import deepcopy

from Domain.rezervare import get_pret


def ordonare(lista):
    """
    Functia ordoneaza descrescator rezervarile
    :param lista: lista
    :return: rezervarile ordonate descrescator
    """
    lista_noua = []
    lista_noua = deepcopy(lista)
    auxiliar = []
    for i in range(0, len(lista_noua)-1):
        for j in range(i+1, len(lista_noua)):

            if get_pret(lista_noua[i]) < get_pret(lista_noua[j]):
                auxiliar = lista_noua[j]
                lista_noua[j] = lista_noua[i]
                lista_noua[i] = auxiliar

    return lista_noua
