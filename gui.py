from tkinter import *
import tkinter as tk
window=tk.Tk()
window.title('Fingervein')
window.geometry('600x600')
window.configure(background='blue')
lb1=Label(window,text='Fingervein',width=10,height=2,bg='black',fg='white',font=('times',30,'bold'))
lb1.place(x=200,y=10)
lb3=Label(window,text='enter text',width=10,bg='black',fg='white',font=('times',15,'bold'))
lb3.place(x=200,y=125)
lb2=Entry(window,text='enter txt',width=10,bg='black',fg='white',font=('times',15,'bold'))
lb2.place(x=350,y=125)


def text():
    ##print("Hello")
    ##lb2=Label(window,text='Hello')
    a=lb2.get()
    lb4=Label(window,text=('The entered text is '+a),width=30,bg='black',fg='white',font=('times',15,'bold'))
    ##print(lb2)
    lb4.place(x=200,y=300)
    
btn1=Button(window,text='click here',command=text,width=10,height=2,bg='black',fg='white',font=('times',15,'bold'))
btn1.place(x=200,y=200)

btn2=Button(window,text='QUIT',command=window.destroy,width=10,height=2,bg='black',fg='white',font=('times',15,'bold'))
btn2.place(x=350,y=200)




window.mainloop()
