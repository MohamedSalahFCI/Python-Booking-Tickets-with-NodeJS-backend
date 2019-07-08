from tkinter import *
import requests
import json
from tkinter import messagebox as m



class userBooking:
    def __init__(self,prewin,username,userid):
        #prewin.destroy()
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

        response=requests.get('https://booking-python.herokuapp.com/api/v1/booking?userId='+str(userid))
        if (response.status_code == 401) or (response.status_code == 422):
            m.showinfo("Error", "Invalid Request Error")
        else:
            mydata=response.json()
            print(mydata)
            subdata=mydata["data"]
            print(subdata[0]["train"]["from"])
            #mafrod ha3mal for 3la l length bta3 l dictionary w b3den ha3mal kolo label 3al3h m3 ta8yeer l index
            for i in range(0,len(subdata),1):
                mydateandtime = subdata[i]["train"]['date']
                mydate = mydateandtime[0:10]
                myTime = mydateandtime[11:16]
                yournumberoftravel=Label(root,text="your "+str(i+1) +" travel :-",width=500,bg="#e60000").pack()
                myfirstTrain=Label(root,text=str(i+1)+"-"+" "+"From "+subdata[i]["train"]["from"]+" "+"To "+subdata[i]["train"]["to"]+"           "+"Date :- "+mydate+" "+"Time:- "+" "+myTime+" "+"Booking Number"+" "+str(subdata[i]["id"]),width=500,bg="white").pack()
                mylabel = Label(root, bg="black").pack()




        root.deiconify()
        root.mainloop()