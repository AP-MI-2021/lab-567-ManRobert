from Tests.test_all import test_all
from UI.console import meniu


def main ():
    lista = []
    test_all()
    print("Toate functiile de calcul au trecut testele ")
    meniu(lista)


if __name__ == '__main__':
    main()