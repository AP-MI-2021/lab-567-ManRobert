def creeaza_rezervare(id, nume, clasa, pret, checkin):
    """
    Functia creeaza o lista ce contine detaliile unei rezervari de zbor la o companie aeriana
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: lista cu detaliile
    """

    return [id, nume, clasa, pret, checkin]


def get_id(rezervare):
    """
    Functia returneaza id-ul unei rezervari
    :param rezervare: dictionar ce contine detaliile unei rezervari
    :return: id-ul rezervarii
    """

    return rezervare[0]


def get_nume(rezervare):
    """
    Functia returneaza numele unei rezervari
    :param rezervare: dictionar ce contine detaliile unei rezervari
    :return: numele unei rezervari
    """

    return rezervare[1]


def get_clasa(rezervare):
    """
    Functia returneaza clasa unei rezervari
    :param rezervare: dictionar ce contine detaliile unei rezervari
    :return: clasa unei rezervari
    """

    return rezervare[2]


def get_pret(rezervare):
    """
    Functia returneaza pretul unei rezervari
    :param rezervare: dictionar ce contine detaliile unei rezervari
    :return: pretul unei rezervari
    """

    return rezervare[3]


def get_checkin(rezervare):
    """
    Functia returneaza Da daca persoana a facut checkin, Nu in caz contrat
    :param rezervare: dictionar ce contine detaliile unei rezervari
    :return: da/nu (ca si string)
    """

    return rezervare[4]


def get_all(rezervare):
    """
    Functia returenaza toate datele
    :param rezervare: dictionar ce contine detaliile unei rezervari
    :return: datele(valorile cheilor)
    """

    return get_id(rezervare), get_nume(rezervare), get_clasa(rezervare), get_pret(rezervare), get_checkin(rezervare)


def to_string(rezervare):
    """
    Functia converteste la string dictionarul
    :param rezervare: dictionar cu detaliile uneor rezervari
    :return: string
    """

    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)

    )
