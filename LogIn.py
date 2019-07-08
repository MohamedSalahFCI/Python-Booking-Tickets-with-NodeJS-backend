from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m
from Details import Details
from AdminDetails import AdminDetails
import requests
import json
def presstologin(username,password,usEntry,passEntry,window):
    if(username=="")and(password==""):
        m.showinfo("Error", "You Must Enter all Information")
        usEntry.configure(background='red')
        passEntry.configure(background='red')
        usEntry.focus()
    elif(username==""):
        m.showinfo("Error", "You Must Enter User Name")
        usEntry.configure(background='red')
        usEntry.focus()
    elif(password==""):
        m.showinfo("Error", "You Must Enter your Password")
        passEntry.configure(background='red')
        passEntry.focus()

    else:
        #hna han3mal l post wel check
        print("mashy")
        myData={
            "username":username,
            "password":password
        }
        response=requests.post('https://booking-python.herokuapp.com/api/v1/signin',data=myData)
        print(response.status_code)
        if(response.status_code==401)or(response.status_code==422):
            m.showinfo("Error", "Invalid UserName And Password")
        else:
            reply=response.json()
            print(reply)
            print(reply['user'])
            print(reply['user']['type'])
            print(reply['user']['id'])
            myuserid=reply['user']['id']
            if(reply['user']['type']=="CLIENT"):
                l = Details(window,username,myuserid)
            elif(reply['user']['type']=="ADMIN"):
                x=AdminDetails(window)



class LogIn:
    def __init__(self,preWin):
        preWin.destroy()
        root = Tk()
        root.title("Log In")
        root.geometry('500x500')
        root.resizable(0, 0)
        root.withdraw()
        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
        root.geometry("+%d+%d" % (x, y))
        root.configure(background='#0d0c0c')
        WindowTitle = Label(root, text="Log in", bg="white", bd=10, fg="Black", padx=50).pack()
        usernamelabel = Label(root, text="User Name :-", bg="white", bd=5).place(x=40, y=90)
        passwordLabel = Label(root, text="Password :-", padx=5, bg="white", bd=5).place(x=40, y=170)


        self.username=StringVar(master=root)
        self.usernameEntry=Entry(root,width=55,bd=4,textvariable=self.username)
        self.usernameEntry.place(x=140,y=90,height=30)
        self.password = StringVar(master=root)
        self.passwordEntry = Entry(root, width=55, bd=4, textvariable=self.password, show="*")
        self.passwordEntry.place(x=140, y=170, height=30)

        w = Canvas(root, cursor='arrow', height=2, width=500).place(x=5, y=300)




        presstologinn = Button(root, text="Login Now", command=lambda: presstologin(self.username.get(),
                                                                                    self.password.get(),
                                                                                    self.usernameEntry,
                                                                                    self.passwordEntry,
                                                                                    root),padx=10, bd=6).place(x=200, y=350)







        root.deiconify()
        root.mainloop()





