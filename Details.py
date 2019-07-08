from tkinter import *
from userBokking import userBooking
from  userAddBooking import addingBooking
from UserDeleteBooking import userdeletebooking

def mybookingpress(window,username,userid):
    x=userBooking(window,username,userid)

def userAddBooking(window,username,userid):
    y=addingBooking(window,username,userid)
def deletemyBooking(window,username,userid):
    z=userdeletebooking(window,username,userid)

class Details:
    def __init__(self,prewin,username,myuserid):
        prewin.destroy()
        root = Tk()
        root.title("Tickets Information Welcome"+" "+username)
        root.geometry('500x500')
        root.resizable(0, 0)
        root.withdraw()
        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
        root.geometry("+%d+%d" % (x, y))
        root.configure(background='#0d0c0c')

        welcomelabel=Label(root,text="Welcom "+username).pack()
        w = Canvas(root, cursor='arrow', height=2, width=500).place(x=5, y=100)
        myOwnbooking=Button(root,text="My Booking",command=lambda :mybookingpress(root,username,myuserid),padx=30,bd=5).place(x=170,y=170)
        AddingBooking=Button(root,text="Adding Booking",command=lambda :userAddBooking(root,username,myuserid),padx=20,bd=5).place(x=170,y=270)
        DeletBooking=Button(root,text="Delete Booking",command=lambda :deletemyBooking(root,username,myuserid),padx=25,bd=5).place(x=170,y=370)





        root.deiconify()
        root.mainloop()