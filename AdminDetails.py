from tkinter import *
from AdminAllBooking import AdminAllBooking
from AddingTrain import AddingTrain
from updateTrainData import UpdateData
from adminDeletingTrain import DeletingTrain


def allBooking(window):
    x=AdminAllBooking(window)

def AddTrain(window):
    y=AddingTrain(window)

def update(window):
    z=UpdateData(window)

def deletingTrain(window):
    u=DeletingTrain(window)

class AdminDetails:
    def __init__(self,prewin):
        prewin.destroy()
        root = Tk()
        root.title("Welcome Admin")
        root.geometry('500x500')
        root.resizable(0, 0)
        root.withdraw()
        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
        root.geometry("+%d+%d" % (x, y))
        root.configure(background='#0d0c0c')

        welcomelabel = Label(root, text="Welcom Admin").pack()
        w = Canvas(root, cursor='arrow', height=2, width=500).place(x=5, y=100)
        Allbooking = Button(root, text="All Booking", command=lambda:allBooking(root) ,padx=30, bd=5).place(x=30, y=190)
        AddingsomeTrains = Button(root, text="Adding Train Date", command=lambda:AddTrain(root) ,padx=15, bd=5).place(x=230, y=190)
        UpdatetrainInfo=Button(root, text="update Booking", command=lambda:update(root) ,padx=20, bd=5).place(x=30, y=250)
        deltingTrain=Button(root, text="Delete Booking", command=lambda:deletingTrain(root) ,padx=20, bd=5).place(x=230, y=250)





        root.deiconify()
        root.mainloop()
