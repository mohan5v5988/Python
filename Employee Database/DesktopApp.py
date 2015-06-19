import tkinter
from tkinter import *
import urllib.request,urllib.parse
import json
from tkinter import messagebox


def loginButPressed():
    values = {'Login' : un_entry.get(), 'Password' : pass_entry.get() }
    url = "http://127.0.0.1:5000/login"
    params = json.dumps(values).encode('utf8')
    req = urllib.request.Request(url,data=params,headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    content = response.read()
    content_string = content.decode("utf-8")
    json_data = json.loads(content_string)
    if json_data['status'] == 'good':
        login_frame.pack_forget()
        allbuttons_frame.pack()
    else:
        messagebox.showinfo("Invalide username or password",json_data['status'])
def addEmpSubmitButtonPressed():
    print("hi")
    values = { "Login": loginname_entry.get(), "Name": name_entry.get(), "Password": password_entry.get(), "Salary": int(salary_entry.get()) }
    url = "http://127.0.0.1:5000/addEmp"
    params = json.dumps(values).encode('utf8')
    req = urllib.request.Request(url,data=params,headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    content = response.read()
    content_string = content.decode("utf-8")
    json_data = json.loads(content_string)
    if json_data['status'] == 'good':
        addEmpBut_frame.pack_forget()
        allbuttons_frame.pack()
        messagebox.showinfo("States","Employee Created")
    else:
        messagebox.showinfo("States","Employee Not Created\nTry Again")
def goBackFromList():
    allbuttons_frame.pack()
    listEmpBut_frame.pack_forget()
def goBackFromAddEmp():
    addEmpBut_frame.pack_forget()
    allbuttons_frame.pack()
def addEmpButton():
    allbuttons_frame.pack_forget()
    addEmpBut_frame.pack()
def listEmpButtonPressed():
    data = ""
    page = urllib.request.urlopen("http://127.0.0.1:5000/allEmp")
    code = page.getcode()
    if code == 200:
        content=page.read()
        content_string = content.decode("utf-8")
        json_data = json.loads(content_string)
        for da in json_data["data"]:
            data += str(da) + "\n"
        scrollbar = tkinter.Scrollbar(listEmpBut_frame)
        text = tkinter.Text(listEmpBut_frame, height=40, width=100)
        scrollbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, fill=Y)
        scrollbar.config(command=text.yview)
        text.config(yscrollcommand=scrollbar.set)
        listEmp_data = data
        text.insert(END, listEmp_data)
        backFromList_button = Button(listEmpBut_frame,text='back', command=goBackFromList)
        backFromList_button.pack()
        allbuttons_frame.pack_forget()
        listEmpBut_frame.pack()
def logoutButPressed():
    allbuttons_frame.pack_forget()
    login_frame.pack()

base = tkinter.Tk()
base.title("Employee")


# this is the login frame
login_frame = tkinter.Frame(base)
un_label = Label(login_frame, text="User Name")
un_label.pack()
un_entry = Entry(login_frame)
un_entry.pack()
pass_label = Label(login_frame, text="Password")
pass_label.pack()
pass_entry = Entry(login_frame)
pass_entry.pack()
login_button = Button(login_frame, text="Login", command=loginButPressed)
login_button.pack()

# this is the next frame when login is successful
allbuttons_frame = tkinter.Frame(base)
addEmp_button = Button(allbuttons_frame,text="Add Employee",command=addEmpButton)
addEmp_button.pack()
listEmp_button = Button(allbuttons_frame,text='List Employees',command=listEmpButtonPressed)
listEmp_button.pack()
logout_button = Button(allbuttons_frame,text='Log Out',command=logoutButPressed)
logout_button.pack()

addEmpBut_frame = tkinter.Frame(base)
loginname_label = Label(addEmpBut_frame,text='Login Name')
loginname_label.pack()
loginname_entry = Entry(addEmpBut_frame)
loginname_entry.pack()
password_lable = Label(addEmpBut_frame,text='Password')
password_lable.pack()
password_entry = Entry(addEmpBut_frame)
password_entry.pack()
name_label = Label(addEmpBut_frame,text='Name')
name_label.pack()
name_entry = Entry(addEmpBut_frame)
name_entry.pack()
salary_lable = Label(addEmpBut_frame,text='Salary')
salary_lable.pack()
salary_entry = Entry(addEmpBut_frame)
salary_entry.pack()
addEmpSubmit_butten = Button(addEmpBut_frame,text='Submit',command=addEmpSubmitButtonPressed)
addEmpSubmit_butten.pack()
goBackFromAddEmp_button = Button(addEmpBut_frame,text='Back',command=goBackFromAddEmp)
goBackFromAddEmp_button.pack()

listEmpBut_frame = tkinter.Frame(base)

login_frame.pack()

base.mainloop()
