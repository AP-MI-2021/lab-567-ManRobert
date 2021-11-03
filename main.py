from Tests.test_all import test_all
from UI.console import meniu


# link pentru Asana : https://app.asana.com/0/home/1201299275391771
from command_line_console import command_line_console


def main():
    lista = []
    test_all()
    print("Toate functiile de calcul au trecut testele ")
    while True:
        optiune = input("Pentru meniu tastati 1, pentru consola de comenzi, tastati 2;"
                        " Pentru a inchide tastati x ")
        if optiune == "1":
            meniu(lista)
        elif optiune == "2":
            command_line_console(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita ")


if __name__ == '__main__':
    main()
