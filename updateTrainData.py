from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m
from Details import Details
import requests

def finishid(window,fullchoosen,s,d,day,month,year,hour,min):
    print("hna fel update")
    if(fullchoosen==""):
        m.showinfo("Message","You Must Select The coloumn u want to change")
    else:
        #lsa ma3dltsh l taree5 wel wa2t
        x=fullchoosen.split((':-'))
        trainid=x[len(x) - 1]
        print(trainid)

        response=requests.get('https://booking-python.herokuapp.com/api/v1/dates/'+str(trainid))
        if (response.status_code == 401) or (response.status_code == 422):
            m.showinfo("Error", "Invalid Request Error")
        else:
            mydata = response.json()
            print(mydata)
            print(mydata["from"])
            source=mydata["from"]
            print(mydata["to"])
            distination=mydata["to"]
            print(mydata["date"])
            mydate=mydata["date"]
            myupdatedata = {
                "date": mydate,
                "from": source,
                "to": distination
            }
            if (s == "") and (d == ""):
                if (int(hour) < 10):
                    hour = '0' + hour
                if (int(min) < 10):
                    min = '0' + min
                if (int(day) < 10):
                    day = '0' + day
                if (int(month) < 10):
                    month = '0' + month
                    # hna han3mal l post ll Api

                FullDate = year + "-" + month + "-" + day + "T" + hour + ":" + min + ":" + "00.00" + "Z"
                myupdatedata = {
                    "date": FullDate,
                    "from": source,
                    "to": distination
                }

            elif(s==""):
                if (int(hour) < 10):
                    hour = '0' + hour
                if (int(min) < 10):
                    min = '0' + min
                if (int(day) < 10):
                    day = '0' + day
                if (int(month) < 10):
                    month = '0' + month
                    # hna han3mal l post ll Api

                FullDate = year + "-" + month + "-" + day + "T" + hour + ":" + min + ":" + "00.00" + "Z"
                myupdatedata={
                    "date":FullDate,
                    "from":source,
                    "to":d
                }
            elif(d==""):
                if (int(hour) < 10):
                    hour = '0' + hour
                if (int(min) < 10):
                    min = '0' + min
                if (int(day) < 10):
                    day = '0' + day
                if (int(month) < 10):
                    month = '0' + month
                    # hna han3mal l post ll Api

                FullDate = year + "-" + month + "-" + day + "T" + hour + ":" + min + ":" + "00.00" + "Z"
                myupdatedata = {
                    "date": FullDate,
                    "from": s,
                    "to": distination
                }

            elif(day=="")or(month==""):
                myupdatedata = {
                    "date": mydate,
                    "from": s,
                    "to": d
                }
            elif(hour=="")or(min==""):
                myupdatedata = {
                    "date": mydate,
                    "from": s,
                    "to": d
                }

            else:
                if (int(hour) < 10):
                    hour = '0' + hour
                if (int(min) < 10):
                    min = '0' + min
                if (int(day) < 10):
                    day = '0' + day
                if (int(month) < 10):
                    month = '0' + month

                FullDate = year + "-" + month + "-" + day + "T" + hour + ":" + min + ":" + "00.00" + "Z"
                myupdatedata={
                    "date":FullDate,
                    "from":s,
                    "to":d
                }

            response2 = requests.put('https://booking-python.herokuapp.com/api/v1/dates/' + str(trainid), data=myupdatedata)
            if (response2.status_code == 401) or (response2.status_code == 422):
                print("anta fel a5er")
                m.showinfo("Error", "Invalid Request Error")
            else:
                m.showinfo("Message","Update successfully")

class UpdateData:
    def __init__(self, preWin):
        #preWin.destroy()
        root = Tk()
        root.title("Update Data Hera")
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
            trainId = []
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
            stringchooselabel=Label(root,text="Select Travel that you want to Update").pack()
            choseendrop.pack()

            fromLabel = Label(root, text="From").place(x=105, y=80)
            self.fromPlace = StringVar(master=root)
            fromcountry = ttk.Combobox(root, textvariable=self.fromPlace, width=30)
            fromcountry['values'] = ('Ismailia',
                                     'Cairo',
                                     'Gharbya',
                                     'Suez',
                                     'Port Saied',
                                     'Sharm El-Shekh',
                                     'Monofya',
                                     'Alexandrya',
                                     'Aswan',
                                     'Asyut',
                                     'Beheira',
                                     'Beni Suef',
                                     'Dakahlia',
                                     'Damietta',
                                     'Faiyum',
                                     'Giza',
                                     'Kafr El Sheikh',
                                     'Luxor',
                                     'Matruh',
                                     'Minya',
                                     'Monufia',
                                     'New Valley',
                                     'North Sinai',
                                     'Qena',
                                     'Red Sea',
                                     'Sharqia',
                                     'Sohag',
                                     'South Sinai')
            fromcountry.place(x=150, y=80)
            toLabel = Label(root, text="To", padx=8).place(x=105, y=120)
            self.toPlace = StringVar(master=root)
            tocountry = ttk.Combobox(root, textvariable=self.toPlace, width=30)
            tocountry['values'] = ('Ismailia',
                                   'Cairo',
                                   'Gharbya',
                                   'Suez',
                                   'Port Saied',
                                   'Sharm El-Shekh',
                                   'Monofya',
                                   'Alexandrya',
                                   'Aswan',
                                   'Asyut',
                                   'Beheira',
                                   'Beni Suef',
                                   'Dakahlia',
                                   'Damietta',
                                   'Faiyum',
                                   'Giza',
                                   'Kafr El Sheikh',
                                   'Luxor',
                                   'Matruh',
                                   'Minya',
                                   'Monufia',
                                   'New Valley',
                                   'North Sinai',
                                   'Qena',
                                   'Red Sea',
                                   'Sharqia',
                                   'Sohag',
                                   'South Sinai')
            tocountry.place(x=150, y=120)
            AgeLabel = Label(root, text="Date of travel :-",  bg="white", bd=2).place(x=40, y=210)

            # l Ayaaaaaam
            self.Day = StringVar(master=root)
            daylabel = Label(root, text="Day").place(x=140, y=215)
            Dayes = ttk.Combobox(root, textvariable=self.Day, width=3)
            Dayes['values'] = list(range(1, 32))
            Dayes.place(x=170, y=215)

            # l Shohoor
            self.Month = StringVar(master=root)
            mounthLabel = Label(root, text="Month").place(x=250, y=215)
            Month = ttk.Combobox(root, textvariable=self.Month, width=3)
            Month['values'] = list(range(1, 13))
            Month.place(x=295, y=215)

            # l snen
            self.Year = StringVar(master=root)
            yearLabel = Label(root, text="Year").place(x=400, y=215)
            Year = ttk.Combobox(root, textvariable=self.Year, width=4)
            Year['values'] = list(range(1970, 2014))
            Year.place(x=430, y=215)
            # timeLabel=Label(root,text="Date").place(x=40,y=300)
            self.hourVar = StringVar(master=root)
            hourLabel = Label(root, text="Hour").place(x=40, y=300)
            hour = ttk.Combobox(root, textvariable=self.hourVar, width=3)
            hour['values'] = list(range(1, 13))
            hour.place(x=80, y=300)
            self.minVar = StringVar(master=root)
            hourLabel = Label(root, text="Minut").place(x=140, y=300)
            hour = ttk.Combobox(root, textvariable=self.minVar, width=3)
            hour['values'] = list(range(1, 60))
            hour.place(x=190, y=300)


            mycheckButton = Button(root, text="update Now",
                                   command=lambda: finishid(root,
                                                            self.choosen.get(),
                                                            self.fromPlace.get(),
                                                            self.toPlace.get(),
                                                            self.Day.get(),
                                                            self.Month.get(),
                                                            self.Year.get(),
                                                            self.hourVar.get(),
                                                            self.minVar.get()
                                                            )).place(x=150, y=350)

            '''
            s=Label(root,text="From").place(x=20,y=100)
            self.source=StringVar(master=root)
            sourceEntry=Entry(root,textvariable=self.source).place(x=50,y=100)
            o = Label(root, text="To").place(x=20, y=150)
            self.distination = StringVar(master=root)
            distEntry = Entry(root, textvariable=self.distination).place(x=50, y=150)
            l = Label(root, text="Date").place(x=20, y=200)
            mycheckButton = Button(root, text="update Now",
                                   command=lambda: finishid(root, self.choosen.get(),
                                                            self.source.get(),
                                                            self.distination.get())).place(x=150, y=300)


        '''
        root.deiconify()
        root.mainloop()