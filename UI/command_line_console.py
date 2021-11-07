from copy import deepcopy

from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from UI.console import show_all


def command_line_console(lista, undo_list, redo_list):
    while True:
        try:
            print("Pentru ajutor tastati help ")
            comanda = input("Dati comanda ")
            if comanda == "help":
                print("Pentru a adauga o noua rezervare scrieti comanda add urmata de datele")
                print("pe care doriti sa le introduceti, separate prin virgula ")
                print("Pentru a modifica,scrieti update,apoi virgula si id-ul rezervarii ce urmeaza")
                print("Sa fie modificata,urmat de noile date")
                print("Pentru a sterge scrieti delete,apoi virgula si id-ul rezerarii ce urmeaza sa se stearga")
                print("Pentru a face undo tastati undo ")
                print("Pentru a face redo tastati redo ")
                print("Pentru a afisa toate datele scrieti showall")
                print("Pentru a iesi scrieti stop")
                print("Puteti scrie mai multe comenzi separandu-le prin ;")
                print("Exemple:")
                print("add,1,Marcel,business,200,Da")
                print("add,2,Ricardo,economy,250.50,Nu")
                print("undo;redo")
                print("showall;")
                print("delete,2;showall")
                print("update,1,Dorel,economy plus,100,Nu")
            else:
                executa_comenzi = comanda.split(";")
                for i in range(len(executa_comenzi)):
                    comanda_separata = executa_comenzi[i].split(",")
                    if comanda_separata[0] == "add":
                        if len(comanda_separata) != 6:
                            raise ValueError("Trebuie sa introduceti exact 5 date! ")
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        clasa = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        checkin = comanda_separata[5]
                        rezultat = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
                        undo_list.append(lista)
                        redo_list.clear()
                        lista = deepcopy(rezultat)
                    elif comanda_separata[0] == "delete":
                        id = comanda_separata[1]
                        rezultat = sterge_rezervare(id, lista)
                        undo_list.append(lista)
                        redo_list.clear()
                        lista = deepcopy(rezultat)
                        print("Au fost sterse date ")
                    elif comanda_separata[0] == "update":
                        if len(comanda_separata) != 6:
                            raise ValueError("Trebuie sa introduceti exact 5 date! ")
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        clasa = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        checkin = comanda_separata[5]
                        rezultat = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
                        undo_list.append(lista)
                        redo_list.clear()
                        lista = deepcopy(rezultat)
                        print("Au fost modificate date")
                    elif comanda_separata[0] == "showall":
                        show_all(lista)
                        print("S-a afisat un set de date ")
                    elif comanda_separata[0] == "undo":
                        if len(undo_list) > 0:
                            redo_list.append(lista)
                            lista = undo_list.pop()
                        else:
                            print("Nu se poate face undo ")
                    elif comanda_separata[0] == "redo":
                        if len(redo_list) > 0:
                            undo_list.append(lista)
                            lista = redo_list.pop()
                        else:
                            print("Nu se poate face redo ")
                    elif comanda_separata[0] == "stop":
                        return lista
                    else:
                        print("Comanda gresita ")
        except ValueError as ve:
            print("Eroare: {}".format(ve))
