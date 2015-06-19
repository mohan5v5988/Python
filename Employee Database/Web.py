__author__ = 'MohanVelaga'

from flask import Flask,jsonify,request,abort
from database import DataBase
from Employee import Employee

app=Flask(__name__)

@app.route('/allEmp', methods=['GET'])
def getEmp():
    data = DataBase.getAllEmp()
    print(data)
    if not data:
        return jsonify({'status':'bad'})
    else:
        return jsonify({'status':'good','data':data})


@app.route('/Emp', methods=['GET'])
def getSingleEmp():
    id = request.args.get('id', '')
    data = DataBase.getByID(id)
    return jsonify({'status':'good','data':data})



@app.route('/addEmp', methods=['POST'])
def createEmp():
    if not request.json:
        abort(400)
    DataBase.createEmp(Employee(0,request.json['Login'],request.json['Name'],Employee.hashPassword(request.json['Password']),request.json['Salary']))
    return jsonify({'status':'good'})

@app.route('/editEmp', methods=['POST'])
def editEmp():
    id = request.args.get('id', '')
    print(request.json)
    if not request.json:
        abort(400)
    DataBase.editEmp(id,Employee(0,request.json['Login'],request.json['Name'],Employee.hashPassword(request.json['Password']),request.json['Salary']))
    return jsonify({'status':'good'})

@app.route('/login', methods=['POST'])
def login():
    print(request.json)
    if not request.json:
        abort(400)
    data = DataBase.isUser(request.json['Login'],Employee.hashPassword(request.json['Password']))
    if not data:
        return jsonify({'status':"Invalide user name or password"})
    else:
        return jsonify({'status':'good','data':data})
"""
@app.route('/deleteEmp/<int:id>', methods=['DELETE'])
def deleteEmp(id):
    DataBase.deleteEmp(id)
    return jsonify({'status':'good'})

"""

app.run(debug = True)
