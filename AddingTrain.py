from tkinter import *
import requests
from tkinter import ttk
from tkinter import messagebox as m



def AddNow(window,fromwhere,tocountry,day,month,year,hour,min):
    if(fromwhere==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(tocountry==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(day==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(month==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(year==""):
        m.showinfo("Error", "You Must Enter all Information")
    else:
        if (int(hour)<10):
            hour='0'+hour
        if (int(min)<10):
            min='0'+min
        if (int(day) < 10):
            day = '0' + day
        if (int(month)<10):
            month='0'+month
            #hna han3mal l post ll Api

        FullDate=year+"-"+month+"-"+day+"T"+hour+":"+min+":"+"00.00"+"Z"
        mydata={
            "from":fromwhere,
            "to":tocountry,
            "date":FullDate
        }
        print(mydata)
        response = requests.post('https://booking-python.herokuapp.com/api/v1/dates',data=mydata)
        reply = response.json()

        print(response.status_code)
        if (response.status_code == 401) or (response.status_code == 422):
            myError = reply["errors"]
            print(myError[0]["msg"])
            if (myError[0]["msg"] == 'to is required'):
                m.showinfo("Error", "Error to Adding")
        else:
            m.showinfo("Message", "Adding successfully")



class AddingTrain:
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
        fromLabel=Label(root,text="From").place(x=105,y=80)
        self.fromPlace=StringVar(master=root)
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
        toLabel = Label(root, text="To",padx=8).place(x=105, y=120)
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
        AgeLabel = Label(root, text="BithDate :-", padx=7, bg="white", bd=5).place(x=40, y=210)

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
        #timeLabel=Label(root,text="Date").place(x=40,y=300)
        self.hourVar=StringVar(master=root)
        hourLabel = Label(root, text="Hour").place(x=40, y=300)
        hour = ttk.Combobox(root, textvariable=self.hourVar, width=3)
        hour['values'] = list(range(1, 13))
        hour.place(x=80, y=300)
        self.minVar = StringVar(master=root)
        hourLabel = Label(root, text="Minut").place(x=140, y=300)
        hour = ttk.Combobox(root, textvariable=self.minVar, width=3)
        hour['values'] = list(range(1, 60))
        hour.place(x=155, y=300)

        Addnewtrain = Button(root, text="Add Travel Now ", command=lambda: AddNow(root,self.fromPlace.get(),
                                                                          self.toPlace.get(),
                                                                          self.Day.get(),
                                                                          self.Month.get(),
                                                                          self.Year.get(),
                                                                           self.hourVar.get(),
                                                                           self.minVar.get()), padx=10, bd=5).place(x=20,y=420)



        root.deiconify()
        root.mainloop()

