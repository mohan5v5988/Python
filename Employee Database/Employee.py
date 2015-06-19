__author__ = 'MohanVelaga'

import hashlib

class Employee :
    def __init__(self,id,login,name,password,salary):
        self.id = id
        self.login = login
        self.name = name
        self.password = password
        self.salary = salary

    def print(self):
        return "ID = " + str(self.id) + " Login = " + self.login + " Name = " + self.name + " Salary = " + str(self.salary) + \
               "\n==========================================================================="
    def getPay(self):
        return self.salary
    def changeToJSON(self):
        return {'ID':self.id,'Name':self.name,'Login':self.login,'Salary':self.salary}
    @staticmethod
    def hashPassword(password):
        m = hashlib.sha256()
        m.update(password.encode('utf-8'))
        return m.digest()