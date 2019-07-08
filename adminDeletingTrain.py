from tkinter import *
import requests
from tkinter import ttk
from tkinter import messagebox as m
import json

def delete(window,fullchoosen):
    #window.destroy()
    x = fullchoosen.split((':- '))
    print(x)
    print(x[len(x) - 1])
    trainid=x[len(x) - 1]
    response = requests.delete('https://booking-python.herokuapp.com/api/v1/dates/'+str(trainid))
    if (response.status_code == 401) or (response.status_code == 422):
        m.showinfo("Error", "Invalid Request Error")
    else:
        m.showinfo("Message", "Travel deleted successfully")


class DeletingTrain:
    def __init__(self,prewin):
        #prewin.destroy()
        root = Tk()
        root.title("Tickets Information Welcome Admin")
        root.geometry('500x500')
        root.resizable(0, 0)
        root.withdraw()
        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
        root.geometry("+%d+%d" % (x, y))
        root.configure(background='#0d0c0c')

        response = requests.get('https://booking-python.herokuapp.com/api/v1/dates')
        if (response.status_code == 401) or (response.status_code == 422):
            m.showinfo("Error", "Invalid Request Error")
        else:
            mydata = response.json()
            print(mydata)
            subdata = mydata["data"]
            # mafrod ha3mal for 3la l length bta3 l dictionary w b3den ha3mal kolo label 3al3h m3 ta8yeer l index
            l = []
            for i in range(0, len(subdata), 1):
                mydateandtime = subdata[i]['date']
                mydate = mydateandtime[0:10]
                myTime = mydateandtime[11:16]
                s = "From " + subdata[i]["from"] + " " + "To " + subdata[i][
                    "to"] + "      " + "Date :-" + mydate + " " + "time:- " + myTime + "By Train Number :-" + " " + str(
                    subdata[i]["id"])
                l.append(s)
            self.choosen = StringVar(master=root)
            choseendrop = ttk.Combobox(root, textvariable=self.choosen, width=80)
            choseendrop['values'] = l
            stringchooselabel = Label(root, text="Select Travel that you want to Delete").pack()
            choseendrop.pack()
            mycheckButton = Button(root, text="Delete Now ",command=lambda: delete(root, self.choosen.get())).place(x=150, y=200)

        root.deiconify()
        root.mainloop()


