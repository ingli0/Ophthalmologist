import tkinter
import sqlite3
rootE=None
var=None


def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
    e1=t1.get()
    e2=t2.get()
    e3=str(var.get())
    e4=t3.get()
    e5=t9.get()
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    e10=t9.get()
    conn = sqlite3.connect("MDBA.db")
    conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "EMPLOYEE DATA ADDED")

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var,t8,t9,t10
    rootE=tkinter.Tk()
    rootE.title("AΠΟΤΕΛΕΣΜΑΤΑ ΕΞΕΤΑΣΕΩΝ")
    rootE.geometry('400x400')
    var = tkinter.StringVar(master=rootE)
    H=tkinter.Label(rootE,text="AΠΟΤΕΛΕΣΜΑΤΑ ΕΞΕΤΑΣΕΩΝ",fg='grey',font="Arial 10 bold")
    H.place(x=50,y=20)
    l1=tkinter.Label(rootE,text="ΑΜΚΑ ΑΣΘΕΝΗ")
    l1.place(x="50",y="50")
    t1=tkinter.Entry(rootE)
    t1.place(x='240',y='50')
    l2 = tkinter.Label(rootE, text="ΟΝΟΜΑ ΑΣΘΕΝΗ")
    l2.place(x=50,y=80)
    t2 = tkinter.Entry(rootE)
    t2.place(x='240', y='80')
    l4 = tkinter.Label(rootE, text="Βαθμος μυωπίας")
    l4.place(x=50,y=140)
    t3=tkinter.Entry(rootE)
    t3.place(x=240,y=140)
    l6=tkinter.Label(rootE,text="βαθμος υπερμετρωπία")
    l6.place(x=50,y=200)
    t4=tkinter.Entry(rootE)
    t4.place(x=240,y=200)
    l7 = tkinter.Label(rootE, text="βαθμος αστιγματισμου")
    l7.place(x=50,y=230)
    t5 = tkinter.Entry(rootE)
    t5.place(x=240,y=230)
    l8 = tkinter.Label(rootE, text="πίεση του κάθε ματιού")
    l8.place(x=50,y=260)
    t6 = tkinter.Entry(rootE)
    t6.place(x=240,y=260)
    l9 = tkinter.Label(rootE, text="κόστος εξετασης")
    l9.place(x=50,y=290)
    t7=tkinter.Entry(rootE)
    t7.place(x=240,y=290)

    l10 = tkinter.Label(rootE, text="ID ΡΑΝΤΕΒΟΥ")
    l10.place(x=50,y=170)
    t9=tkinter.Entry(rootE)
    t9.place(x=240,y=170)

    l11 = tkinter.Label(rootE, text="Βαθμος πρεσβυωπία")
    l11.place(x=50,y=110)
    t10=tkinter.Entry(rootE)
    t10.place(x=240,y=110)

    b1=tkinter.Button(rootE,text="SAVE",command=inp)
    b1.place(x=60,y=320)
    b2=tkinter.Button(rootE,text="DELETE EMPLOYEE",command=delo)
    b2.place(x=110,y=320)
    b3=tkinter.Button(rootE,text="EXIT",command=ex)
    b3.place(x=230,y=320)
    rootE.mainloop()

def delling():
    global d1,de
    de=str(d1.get())
    conn = sqlite3.connect("MDBA.db")
    p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
    if (len(p) != 0):
        conn.execute("DELETE from employee where EMP_ID=?", (de,))
        dme = tkinter.Label(rootDE, text="EMPLOYEE DELETED FROM DATABASE", fg="green")
        dme.place(x=20, y=100)
        conn.commit()
    else:
        error = tkinter.Label(rootDE, text="EMPLOYEE DOESN'T EXIST", fg="Red")
        error.place(x=20, y=100)

rootDE=None
def delo():
    global rootDE,d1
    rootDE=tkinter.Tk()
    rootDE.geometry("250x250")
    rootDE.title("EMPLOYEE DELETION")
    h1=tkinter.Label(rootDE,text="ENTER EMPLOYEE ID TO DELETE :")
    h1.place(x=20,y=10)
    d1=tkinter.Entry(rootDE)
    d1.place(x=20,y=40)
    B1=tkinter.Button(rootDE,text="DELETE",command=delling)
    B1.place(x=20,y=70)
    rootDE.mainloop()


