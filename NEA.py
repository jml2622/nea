import tkinter as tk 
from tkinter import ttk 
from tkinter import *
from tkinter.ttk import Combobox


users = {"Alfred":"Password",
         "Ryan":"yaar",
         "Jane":"123"}


class LoginScreen:



    def __init__(self,window):
        self.window = window
        self.username = StringVar()
        self.password = StringVar()
        window.title("Encrypted Messaging Service")
        self.txtfld1=Entry(window, textvariable=self.username)
        self.lbl1=Label(window, text="Username")
        self.txtfld1.place(x=100, y=100)
        self.lbl1.place(x=25, y=100)
        self.txtfld2=Entry(window, textvariable=self.password)
        self.lbl2=Label(window, text="Password")
        self.txtfld2.place(x=100, y=200)
        self.lbl2.place(x=25, y=200)
        self.btn=Button(window, text="submit", command=self.fetch)
        self.btn.place(x=25, y=300)
        self.btn=Button(window, text="cancel",command=self.complete)
        self.btn.place(x=200, y=300)
        self.btn=Button(window,text ="i forgor",command=self.forgor)
        self.btn.place(x = 100, y = 400)

    def fetch(self):
        self.username = self.txtfld1.get()
        self.password = self.txtfld2.get()
        print(self.username)
        print(self.password)
        self.submit(self.window)
        
    def complete (self):
        self.window.destroy()

    def forgor(self):
        self.lbl4=Label(window, text = "wa wa get melonated", font=("Comic Sans", 22))
        self.lbl4.place(x=100, y = 150)

    def submit (self, window):
        if self.username =="" or self.password == "":
            print (self.username, self.password)
            self.lbl3=Label(window, text="Please enter a username or password", fg = 'red')
            self.lbl3.place(x=100, y = 50)
        else:
            print("here")
            if self.username in users:
                print("yay")
                if users[self.username] == self.password:
                    print("youve won")
                else:
                    self.lbl5=Label(window, text="password incorrect", fg = 'red')
                    self.lbl5.place(x=100, y = 50)
            else:
                self.lbl6=Label(window, text="user not found", fg = 'red')
                self.lbl6.place(x=100, y = 50)


window=Tk()
LoginScreen(window)
window.geometry("600x600+10+20")
window.mainloop()



#class Loadingwindow(Toplevel):
   #def __init__(self,window2):
       #super()•__init__(window2 = window2)
       #self.title("Logging in ...")
       #self.lbl3=Label(window, text="downloading messages please wait")
       #self.lbl3.place(x=100, y = 100)
       
       


#window2=Tk
#Loadingwindow(window2)
#WIDTH = 100
#HEIGHT = 75
#window2.mainloop()

