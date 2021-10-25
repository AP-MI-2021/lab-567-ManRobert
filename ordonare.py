from Domain.rezervare import get_pret, to_string


def ordonare(lista):
    """
    Functia ordoneaza descrescator rezervarile
    :param lista: lista
    :return: rezervarile ordonate descrescator
    """

    auxiliar = []
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):

            if get_pret(lista[i]) < get_pret(lista[j]):
                auxiliar = lista[j]
                lista[j] = lista[i]
                lista[i] = auxiliar

    return lista