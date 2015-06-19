__author__ = 'MohanVelaga'

import os
import sqlite3
from Employee import Employee

class DataBase:
    #DBName = "Employee.sqlite"
    DBName = "mm.sqlite"
    @staticmethod
    def createTable():
        conn = sqlite3.connect(DataBase.DBName)
        cursor = conn.cursor()
        cursor.execute("create table Employee (id INTEGER PRIMARY KEY,login text,name text,password text,salary INTEGER)")
        conn.commit()
        conn.close()
    @staticmethod
    def isFile():
        if os.path.isfile(DataBase.DBName) : return True
        return False
    @staticmethod
    def isUser(login,password):
        data = []
        conn = sqlite3.connect(DataBase.DBName)
        cursor = conn.cursor()
        result = cursor.execute("select * from Employee where login = ? and password = ? ",(login,password))
        for r in result:
            data.append(Employee(r[0],r[1],r[2],r[3],r[4]).changeToJSON())
        return data
    @staticmethod
    def getAllEmp():
        data = []
        conn = sqlite3.connect(DataBase.DBName)
        cursor = conn.cursor()
        result = cursor.execute("select * from Employee")
        for r in result:
            data.append(Employee(r[0],r[1],r[2],r[3],r[4]).changeToJSON())
        conn.close()
        return data
    @staticmethod
    def getByID(id):
        conn = sqlite3.connect(DataBase.DBName)
        cursor = conn.cursor()
        result = cursor.execute("select * from Employee where id = "+str(id))
        data = []
        for r in result:
            data.append(Employee(r[0],r[1],r[2],r[3],r[4]).changeToJSON())
        conn.close()
        return data
    @staticmethod
    def createEmp(emp):
        conn = sqlite3.connect(DataBase.DBName)
        cursor = conn.cursor()
        cursor.execute("insert into Employee (id, name, login, password, salary) values (NULL,?, ?, ?, ?) ",(emp.name,emp.login,emp.password,emp.salary))
        conn.commit()
        conn.close()
    @staticmethod
    def editEmp(id,emp):
        conn = sqlite3.connect(DataBase.DBName)
        cursor = conn.cursor()
        cursor.execute("update Employee SET name = ?, login = ?, password = ?, salary = ? where id = ? ",(emp.name,emp.login,emp.password,emp.salary,id))
        conn.commit()
        conn.close()
    @staticmethod
    def deleteEmp(id):
        conn = sqlite3.connect(DataBase.DBName)
        cursor = conn.cursor()
        cursor.execute("delete from Employee where id = ? ",(id))
        conn.commit()
        conn.close()