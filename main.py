from Tests.test_all import test_all
from UI.console import meniu


# link pentru Asana : https://app.asana.com/0/home/1201299275391771
from command_line_console import command_line_console


def main():
    lista = []
    test_all()
    print("Toate functiile de calcul au trecut testele ")
    command_line_console(lista)

if __name__ == '__main__':
    main()
