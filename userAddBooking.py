from tkinter import *
import requests
from tkinter import ttk
import json
from tkinter import messagebox as m

def finishid(window,fullchoosen,userid):
    #3ayez l id bta3 l user shan a3raf a3mal add
    #window.destroy()
    x=fullchoosen.split((':- '))
    print(x)
    print(x[len(x)-1])
    print(userid)
    mydata={
        "train":x[len(x)-1],
        "user":userid
    }
    response=requests.post('https://booking-python.herokuapp.com/api/v1/booking',data=mydata)
    response.json()
    if (response.status_code == 401) or (response.status_code == 422):
        m.showinfo("Error", "Invalid Request Error")
    else:
        m.showinfo("Message", "Adding success")





class addingBooking():
    def __init__(self, prewin, username, userid):
        #prewin.destroy()
        root = Tk()
        root.title("Tickets Information Welcome" + " " + username)
        root.geometry('500x500')
        root.resizable(0, 0)
        root.withdraw()
        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
        root.geometry("+%d+%d" % (x, y))
        root.configure(background='#0d0c0c')
        #gettrain date
        #ba3d ma5tart mn l combo box hageb l atrr w haykon = l id bta3 l train aly gayli mn gettrain date w lma adoos 3la l zorar hab3t l id bta3 l user wel id dh
        response = requests.get('https://booking-python.herokuapp.com/api/v1/dates')
        if (response.status_code == 401) or (response.status_code == 422):
            m.showinfo("Error", "Invalid Request Error")
        else:
            mydata = response.json()
            print(mydata)
            subdata = mydata["data"]
            # mafrod ha3mal for 3la l length bta3 l dictionary w b3den ha3mal kolo label 3al3h m3 ta8yeer l index
            l=[]
            for i in range(0, len(subdata), 1):
                mydateandtime = subdata[i]['date']
                mydate = mydateandtime[0:10]
                myTime = mydateandtime[11:16]
                s= "From " +subdata[i]["from"]+" "+"To "+subdata[i]["to"]+"      "+"Date :-"+mydate+" "+"time:- "+myTime+"By Train Number :-"+" "+str(subdata[i]["id"])
                l.append(s)
            self.choosen=StringVar(master=root)
            choseendrop=ttk.Combobox(root,textvariable=self.choosen,width=80)
            choseendrop['values']=l
            stringchooselabel = Label(root, text="Select Travel that you want to Booking").pack()
            choseendrop.pack()

            mycheckButton=Button(root,text="Booking Now",command=lambda :finishid(root,self.choosen.get(),userid)).place(x=150,y=200)


            '''
            for i in range(0, len(subdata), 1):
                myfirstTrain = Label(root,
                                     text=str(i + 1) + "-" + " " + "From " + subdata[i]["from"] + " " + "To " +subdata[i]["to"] + "           " + "Date :- " + mydate + " " + "Time:- " + " " + myTime).pack()
            '''

        root.deiconify()
        root.mainloop()