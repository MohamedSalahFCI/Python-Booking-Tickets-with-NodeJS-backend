from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m
import requests

def delteBooking(fullchosen):
    if(fullchosen==""):
        m.showerror("Error","You Must Choose Travel that u want to delete")
    else:
        print(fullchosen)
        x = fullchosen.split((':- '))
        bookingid = x[len(x) - 1]
        print(bookingid)
        response=requests.delete('https://booking-python.herokuapp.com/api/v1/booking/'+str(bookingid))
        if (response.status_code == 401) or (response.status_code == 422):
            m.showinfo("Error", "Invalid Request Error")
        else:
            m.showinfo("Message","Booking Deleted Successfully")

class userdeletebooking:
    def __init__(self,preWin,username,userid):
        #preWin.destroy()
        root = Tk()
        root.title("Delte Booking of user"+" "+username)
        root.geometry('500x500')
        root.withdraw()
        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
        root.geometry("+%d+%d" % (x, y))
        root.configure(background='#0d0c0c')



        response=requests.get('https://booking-python.herokuapp.com/api/v1/booking?userId='+str(userid))
        if (response.status_code == 401) or (response.status_code == 422):
            m.showinfo("Error", "Invalid Request Error")
        else:
            mydata = response.json()
            print(mydata)
            subdata = mydata["data"]
            print(subdata[0]["train"]["from"])
            mydateandtime = subdata[0]["train"]['date']
            print(mydateandtime)
            mydate = mydateandtime[0:10]
            myTime = mydateandtime[11:16]
            l = []
            for i in range(0, len(subdata), 1):

                s = str(i+1)+"-"+" "+"From "+subdata[i]["train"]["from"]+" "+"To "+subdata[i]["train"]["to"]+"           "+"Date :- "+mydate+" "+"Time:- "+" "+myTime+" "+"Booking Number:-"+" "+str(subdata[i]["id"])
                l.append(s)
            self.choosen = StringVar(master=root)
            choseendrop = ttk.Combobox(root, textvariable=self.choosen, width=80)
            choseendrop['values'] = l
            stringchooselabel=Label(root,text="Select Travel that you want to delete").pack()
            choseendrop.pack()

            delButtone=Button(root,text="Delete Now",command=lambda :delteBooking(self.choosen.get())).place(x=100,y=100)






        root.deiconify()

        root.mainloop()

