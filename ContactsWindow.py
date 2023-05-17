from tkinter import *
#from NEA import *

file=open("Users.txt")
data=file.read().split("/n")
userIDs= []
firstnames=[]
lastnames=[]
positions=[]
for line in data:
     print (line)
     userID, firstname, lastname, position= line.split(":::")
     userIDs.append(userID)
     firstnames.append(firstname)
     lastnames.append(lastname)
     positions.append(position)
    
print(userIDs)

# "add" button where you type in user number then request the data from the server which will find that users data and append it to Users.txt
    

#first name, last name, position, new messages
 
# file = open("contacts_list.txt", "r")

# for line in file:
#     contacts.append(line.strip())

# file.close()
# print(contacts)

class ContactsWindow():
    search = StringVar
    add = StringVar
    def __init__ (self,window):
        self.txtfld1=Entry(window, textvariable=self.search)
        self.lbl1=Label(window, text="Search Userbase")
        self.txtfld1.place(x=150, y=100)
        self.lbl1.place(x=25, y=100)
        self.btn=Button(window, text="search", command=self.search)
        self.btn.place(x=350, y=100)
        self.btn=Button(window,text="add")
        self.btn.place(x = 350,  y = 200 )
        self.txtfld2=Entry(window, textvariable=self.add)
        self.txtfld2.place(x=150, y = 200)
        self.lbl2=Label(window, text = "Add User")
        self.lbl2.place(x=25, y=200)

        data=["Home Insurance Team",
               "Admins", 
               "goofy", 
               "place"]

        self.clicked = StringVar()

        self.clicked.set("Groupchats")
        
        self.option_menu= OptionMenu(window, self.clicked, *data)

        self.option_menu.place(x=100, y=300)

        #self.btn=Button(window)



    def search(self):
        print("goofy aahh")

f = open ("example.txt","r")
print(f.read())




window=Tk()
ContactsWindow(window)
window.geometry("600x600+10+20")
window.mainloop()


