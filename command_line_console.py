from Logic.CRUD import adauga_rezervare,sterge_rezervare
from UI.console import show_all


def command_line_console(lista):
    while True:
        try:
            print("Pentru ajutor tastati help ")
            comanda = input("Dati comanda ")
            if comanda == "help":
                print("Pentru a adauga o noua rezervare scrieti comanda add urmata de datele")
                print("pe care doriti sa le introduceti, separate prin virgula ")
                print("Puteti scrie mai multe comenzi separandu-le prin ;")
                print("Exemple: add,1,'nr 25,25.3,11.02.2021,'alte cheltuieli';")
                print("add,2,'nr 27',24.9,12.10.2021,'canal';")
                print("showall;"
                      "delete,2;"
                      "showall")
                print("update,1,'nr 25', 333.2,11.02.2021,'alte cheltuieli'")
                print("stop pentru iesi")
            elif comanda == "stop":
                break
            else:
                executa_comenzi = comanda.split(";")
                for i in range(len(executa_comenzi)):
                    comanda_separata = executa_comenzi[i].split(",")
                    if comanda_separata[0] == "add":
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        clasa = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        checkin = comanda_separata[5]
                        lista = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
                    elif comanda_separata[0] == "delete":
                        id = comanda_separata[1]
                        lista = sterge_rezervare(id, lista)
                    elif comanda_separata[0] == "update":
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        clasa = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        checkin = comanda_separata[5]
                        lista = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
                    elif comanda_separata[0] == "showall":
                        show_all(lista)
        except ValueError as ve:
            print("Eroare: {}".format(ve))


