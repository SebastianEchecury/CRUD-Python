import datetime as dt

class Employee:
    id = 0
    name = ''
    lastName = ''
    job = ''
    birthDate = ''

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        return self.lastName

    def setJob(self, job):
        self.job = job

    def getJob(self):
        return self.job

    def setBirthDate(self, birthDate):
        self.birthDate = birthDate

    def getBirthDate(self):
        return self.birthDate

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

#    def getAge(self):
#        aux = dt.date.today()-self.getBirthDate()
#        return aux

    def __str__(self):
        str = 'ID: {0} - Employee Name: {1}, {2}. Job: {3}'.format(self.getID(), self.getLastName(), self.getName(), self.getJob())
        return str