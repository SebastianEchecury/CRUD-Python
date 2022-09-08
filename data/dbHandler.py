import mysql.connector
from entities import Employee as emp

class dbHandler:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'seba'
        self.database = 'crud-python'

    def getConnection(self):
        mydb = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        return mydb

    def newE(self, e):
        mydb = self.getConnection()
        cursor = mydb.cursor()
        sql = "INSERT INTO employees (name, lastname, job, birthdate) VALUES (%s, %s, %s, %s)"
        val = (e.getName(), e.getLastName(), e.getJob(), e.getBirthDate())
        cursor.execute(sql, val)
        mydb.commit()
        cursor.close()
        mydb.close()
        return cursor.lastrowid

    def list(self):
        employees = list()

        mydb = self.getConnection()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()

        if result != []:
            for x in result:
                e = emp.Employee()

                e.setID(x[0])
                e.setName(x[1])
                e.setLastName(x[2])
                e.setJob(x[3])
                e.setBirthDate(x[4])

                employees.append(e)

        cursor.close()
        mydb.close()
        return employees

    def search(self, e):
        em = None
        mydb = self.getConnection()
        cursor = mydb.cursor()

        sql = 'SELECT * FROM employees WHERE id = %s'
        val = (e.getID(),)
        cursor.execute(sql, val)
        result = cursor.fetchone()

        if result is not None:
            em = emp.Employee()
            em.setID(result[0])
            em.setName(result[1])
            em.setLastName(result[2])
            em.setJob(result[3])
            em.setBirthDate(result[4])

        cursor.close()
        mydb.close()
        return em

    def delete(self, e):
        deleted = 0
        mydb = self.getConnection()
        cursor = mydb.cursor()

        sql = 'DELETE FROM employees WHERE id = %s'
        val = (e.getID(),)
        cursor.execute(sql, val)
        mydb.commit()
        deleted = cursor.rowcount

        cursor.close()
        mydb.close()
        return deleted

    def update(self, e):
        mydb = self.getConnection()
        cursor = mydb.cursor()

        sql = 'UPDATE employees SET name = %s, lastname = %s, job = %s, birthdate = %s WHERE id = %s'
        val = (e.getName(), e.getLastName(), e.getJob(), e.getBirthDate(), e.getID())
        cursor.execute(sql, val)
        mydb.commit()
        updated = cursor.rowcount

        cursor.close()
        mydb.close()
        return updated