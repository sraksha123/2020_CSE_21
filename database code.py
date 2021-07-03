from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as ttk


def insert():
    name=e_name.get();
    phone=e_phone.get();
    email=e_email.get();
    gender=var.get()
    if gender == 1:
        gender1="male"
    if gender == 2:
        gender1="female"

    if(name=="" or phone==""):
        MessageBox.showinfo("Insert","All fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="student")
        cursor=con.cursor()
        cursor.execute("Insert into student values('"+ name +"','"+ email +"','"+ phone +"','"+gender1+"')")
        cursor.execute("commit");

        MessageBox.showinfo("Insert","Inserted Successfully");
        con.close();

def get():
    con=mysql.connect(host="localhost",user="root",password="",database="student")
    cursor=con.cursor()
    cursor.execute("Select * from student where email='"+e_email.get()+"'")
    rows = cursor.fetchall()

    for row in rows:
        e_name.insert(0,row[1])
        e_phone.insert(0,row[2])
    con.close();

#def show():
    #con=mysql.connect(host="localhost",user="root",password="",database="student")
    #cursor=con.cursor()
    #cursor.execute("Select * from student ")
    #rows = cursor.fetchall()

    #for row in rows:
        #insertData = str(row[0])+'       '+row[1]
        #list.insert(list.size()+1,insertData)
   # con.close()
    
    
root = Tk()
root.geometry("800x500")
root.title("Python - Basic Register Form")
root.configure(background ="Lightblue")
BG = PhotoImage(file = 'bg3.png')
label = ttk.Label(root, image = BG ,bd=0)

def nextPage():
    root.destroy()
    import Main_Gui


lbl = Label(root, text="FINGER VEIN RECOGNITION",width=25  ,height=1  ,fg="Black"  ,bg="light blue" ,font=('italic', 30, ' bold ') ) 
lbl.place(x=400, y=2)

name=Label(root,text='Enter Name',width=15  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold '))
name.place(x=500,y=150)

email=Label(root,text='Enter Email',width=15  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold '))
email.place(x=500,y=200)

phone=Label(root,text='Enter Phone',width=15  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold '))
phone.place(x=500,y=250)

gender=Label(root,text='Enter Gender',width=15  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold '))
gender.place(x=500,y=300)

e_name=Entry(root,width=20  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ') )
e_name.place(x=710,y=150)

e_email=Entry(root,width=20  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ') )
e_email.place(x=710,y=200)

e_phone=Entry(root,width=20  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ') )
e_phone.place(x=710,y=250)

var = IntVar()
    
Radiobutton(root, text="Male",padx = 5, variable=var, value=1,width=5  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold ')).place(x=710,y=300)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2,width=5  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold ')).place(x=830,y=300)

insert=Button(root,text="insert",command=insert,bg="cyan",font=('italic', 15, ' bold '))
insert.place(x=710,y=400)

button1 = Button(text="Fetch",command=nextPage, bg="cyan",font=('Arial', 15, ' bold '))
button1.place(x=710,y=450)

#delete=Button(root,text="delete",font=("italic",10),bg="white",command=delete)
#delete.place(x=70,y=140)

#update=Button(root,text="update",font=("italic",10),bg="white",command=update)
#update.place(x=130,y=140)

get=Button(root,text="View",bg="cyan",font=('Arial', 15, ' bold '),command=get)
get.place(x=710,y=500)

#list=Listbox(root)
#list.place(x=1000,y=150)
#show()

root.mainloop()
