from entities import Employee as emp
from data import dbHandler as dbh
import datetime as dt

class Menu:

    def start(self):
        cmd = self.menu()
        while cmd.lower() != 'exit':
            if cmd == 'list':
                self.list()
            elif cmd == 'search':
                self.search()
            elif cmd == 'new':
                self.newE()
            elif cmd == 'delete':
                self.delete()
            elif cmd == 'update':
                self.update()
            elif cmd == 'exit':
                pass
            cmd = self.menu()
            print(cmd)

    def update(self):
        db = dbh.dbHandler()
        e = emp.Employee()

        print('Input id to update: ', end='')
        e.setID(int(input()))

        em = db.search(e)
        print(em)
        if em is not None:
            self.loadData(em)
            if db.update(em) >= 1:
                print('Record updated')
        else:
            print('ID not found')

    def delete(self):
        db = dbh.dbHandler()
        e = emp.Employee()

        print('Input id to delete: ', end='')
        e.setID(int(input()))

        if db.delete(e) > 0:
            print('Record deleted')
        else:
            print('Couldnt delete record')

    def search(self):
        db = dbh.dbHandler()
        e = emp.Employee()

        print('Input search id: ', end='')
        e.setID(int(input()))
        em = db.search(e)
        if em is not None:
            print(em)
        else:
            print('ID not found')

    def list(self):
        db = dbh.dbHandler()
        for e in db.list():
            print("{}".format(e))

    def menu(self):
        print("Input command: list/search/new/delete/update/exit")
        return input()

    def newE(self):
        db = dbh.dbHandler()
        e = emp.Employee()
        self.loadData(e)
        print("1 record inserted, ID:", db.newE(e))


    def loadData(self, e):
        print('New Employee')
        print('Name: ', end='')
        e.setName(input())
        print('Lastname: ', end='')
        e.setLastName(input())
        print('Job: ', end='')
        e.setJob(input())
        print('Birth Date (YYYY-MM-DD): ', end='')
        dateb = input().split('-')
        e.setBirthDate(birthDate = dt.date(int(dateb[0]), int(dateb[1]), int(dateb[2])))

