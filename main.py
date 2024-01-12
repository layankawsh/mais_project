from tkinter import *
mm= Tk()
def btnclickE():
    global ll
    global name
    global age
    global phone
    ll = Tk()
    l= Label()
    t1 = Label(ll, text="Enter your name ", fg="#7f7336", font=("calibri", 30))
    name = Entry(ll)
    t2 = Label(ll, text="Enter your age ", fg="#7f7336", font=("calibri", 30))
    age = Entry(ll)
    t3 = Label(ll, text="Enter your phone number ", fg="#7f7336", font=("calibri", 30))
    t4 = Button(ll, text="Done", font=("calibri", 30), background="#7f7336", command=doneE)
    phone = Entry(ll)
    t1.pack()
    name.pack()
    t2.pack()
    age.pack()
    t3.pack()
    phone.pack()
    t4.pack(pady=20)
def btnclickF():
    global ll
    global name
    global age
    global phone
    ll = Tk()
    l= Label()
    t1 = Label(ll, text="Enter your name ", fg="#7f7336", font=("calibri", 30))
    name = Entry(ll)
    t2 = Label(ll, text="Enter your age ", fg="#7f7336", font=("calibri", 30))
    age = Entry(ll)
    t3 = Label(ll, text="Enter your phone number ", fg="#7f7336", font=("calibri", 30))
    t4 = Button(ll, text="Done", font=("calibri", 30), background="#7f7336", command=doneF)
    phone = Entry(ll)
    t1.pack()
    name.pack()
    t2.pack()
    age.pack()
    t3.pack()
    phone.pack()
    t4.pack(pady=20)
def btnclickT():
    global ll
    global name
    global age
    global phone
    ll = Tk()
    l = Label()
    t1 = Label(ll, text="Enter your name ", fg="#7f7336", font=("calibri", 30))
    name = Entry(ll)
    t2 = Label(ll, text="Enter your age ", fg="#7f7336", font=("calibri", 30))
    age = Entry(ll)
    t3 = Label(ll, text="Enter your phone number ", fg="#7f7336", font=("calibri", 30))
    t4 = Button(ll, text="Done", font=("calibri", 30), background="#7f7336", command=doneT)
    phone = Entry(ll)
    t1.pack()
    name.pack()
    t2.pack()
    age.pack()
    t3.pack()
    phone.pack()
    t4.pack(pady=20)

def doneT():
    myfile = open("Turkish.txt", "r")
    alldata = myfile.readlines()
    n = name.get()
    a = age.get()
    p = phone.get()
    for x in alldata:
        data = x.split(",")
        if p not in data:
            myfile3 = open("Turkish.txt", "a")
            tt = (n, ",", a, ",", p, "end\n")
            myfile3.writelines(tt)
            myfile3.close()
    myfile.close()

def doneE():
    myfile = open("English.txt", "r")
    alldata = myfile.readlines()
    n = name.get()
    a = age.get()
    p = phone.get()
    for x in alldata:
        data = x.split(",")
        if p not in data:
            myfile1 = open("English.txt", "a")
            tt = (n, ",", a, ",", p, "end\n")
            myfile1.writelines(tt)
            myfile1.close()
    myfile.close()

def doneF():
    myfile = open("French.txt", "r")
    alldata = myfile.readlines()
    n = name.get()
    a = age.get()
    p = phone.get()
    for x in alldata:
        data = x.split(",")
        if p not in data:
            myfile2 = open("French.txt", "a")
            tt = (n, ",", a, ",", p, "end\n")
            myfile2.writelines(tt)
            myfile2.close()

    myfile.close()

myfile1 = open("English.txt", "a")
myfile1.writelines(". ")
myfile2 = open("French.txt", "a")
myfile2.writelines(". ")
myfile3 = open("Turkish.txt", "a")
myfile3.writelines(".")

b1=Label(mm,text="Language learning center",fg="#7f7336",font=("calibri",50))
b2 = Button(mm, text="English",font=("Courier New", 50), background="#7f7336",command=btnclickE)
b3 = Button(mm, text="Turkish", font=("Courier New", 50), background="#7f7336",command=btnclickT)
b4 = Button(mm, text="French",font=("Courier New", 50), background="#7f7336",command=btnclickF)
b1.pack(pady=30)
# b5.pack(pady=10)
b2.pack(pady=30)
b3.pack(pady=30)
b4.pack(pady=30)
mm.mainloop()
