from Tests.test_all import test_all
from UI.command_line_console import command_line_console
from UI.console import meniu


# link pentru Asana : https://app.asana.com/0/home/1201299275391771


def main():
    lista = []
    test_all()
    undo_list = []
    redo_list = []
    print("Toate functiile de calcul au trecut testele ")
    while True:
        print("Pentru meniu tastati 1 ")
        print("Pentru consola de comenzi tastati 2 ")
        print("Pentru a inchide tastati x ")
        optiune = input()
        if optiune == "1":
            meniu(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = command_line_console(lista, undo_list, redo_list)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita ")


if __name__ == '__main__':
    main()
