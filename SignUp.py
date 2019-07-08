from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m
from LogIn import LogIn
import requests
import json








def loginNow(username,email,password,day,month,year,country,phonenum,window):

    if(username==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(email==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(password==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(day==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(month==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(year==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(country==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif(phonenum==""):
        m.showinfo("Error", "You Must Enter all Information")

    else:

        if (int(day) < 10):
            day = '0' + day
        if (int(month)<10):
            month='0'+month
            #hna han3mal l post ll Api

        birthdayDate=year+"-"+month+"-"+day

        mydata={
            "username":username,
            "country":country,
            "email":email,
            "phone":phonenum,
            "birthday":birthdayDate,
            "password":password
        }
        #data=json.dumps(mydata)
        response=requests.post('https://booking-python.herokuapp.com/api/v1/signup',data=mydata)
        print(response.status_code)
        reply=response.json()
        print(reply)
        if(response.status_code==401)or(response.status_code==422):
            myError=reply["errors"]
            print(myError[0]["msg"])
            if(myError[0]["msg"]=='username duplicated'):
                m.showinfo("Error", "Invalid User Name .. Enter Anotherone")
        else:
                goToLogin = LogIn(window)



        '''
        myerror=reply["error"]
        if(myerror[0]["msg"]=="username duplicated"):
            m.showinfo("Error", "Duplicated User Name")
        else:
            # han3mal l satr dh lw l data 3mlha post mazboot
            goToLogin = LogIn(window)
            m.showinfo("Error", "Sign Up successfuly")
        '''
def haveAcc(window):
    print("Hi My Lovely User")
    l=LogIn(window)

'''
def prinNamme( username,email,password,day,month,year,phonenum):
    print(username)
    print(email)
    print(password)
    
    print(day)
    print(month)
    print(year)
    print("Full Date")
    fulldata=day+"/"+month+"/"+year
    print(fulldata)
    print(phonenum)
'''
class SignUp:
    def __init__(self):
        root=Tk()
        root.title("Sign Up")
        root.geometry('500x500')
        root.resizable(0, 0)
        root.withdraw()
        root.update_idletasks()
        x=(root.winfo_screenwidth()-root.winfo_reqwidth())/2.5
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
        root.geometry("+%d+%d" % (x, y))
        root.configure(background='#0d0c0c')
        WindowTitle=Label(root,text="Sign Up",bg="white",bd=10,fg="Black",padx=50).pack()
        usernamelabel = Label(root, text="User Name :-",bg="white",bd=5).place(x=40,y=90)
        EmailLabel=Label(root,text="Email :-",padx=15,bg="white",bd=5).place(x=40,y=130)
        passwordLabel=Label(root,text="Password :-",padx=5,bg="white",bd=5).place(x=40,y=170)
        AgeLabel=Label(root,text="BithDate :-",padx=7,bg="white",bd=5).place(x=40,y=210)
        countryLabel=Label(root,text="Country :-",padx=10,bg="white",bd=5).place(x=40,y=250)
        phoneNumberLabel=Label(root,text="phoneNum :-",bg="white",bd=5).place(x=40,y=290)


        self.username=StringVar(master=root)
        usernameEntry=Entry(root,width=55,bd=4,textvariable=self.username).place(x=140,y=90,height=30)
        self.Email = StringVar(master=root)
        EmailEntry = Entry(root, width=55, bd=4,textvariable=self.Email).place(x=140, y=130, height=30)
        self.password = StringVar(master=root)
        passwordEntry = Entry(root, width=55, bd=4,textvariable=self.password,show="*").place(x=140, y=170, height=30)
        #han3mal l 7aga bta3t l Age
        #l Ayaaaaaam
        self.Day=StringVar(master=root)
        daylabel=Label(root,text="Day").place(x=140,y=215)
        Dayes=ttk.Combobox(root,textvariable=self.Day,width=3)
        Dayes['values']=list(range(1,32))
        Dayes.place(x=170,y=215)

        #l Shohoor
        self.Month=StringVar(master=root)
        mounthLabel=Label(root,text="Month").place(x=250,y=215)
        Month=ttk.Combobox(root,textvariable=self.Month,width=3)
        Month['values']=list(range(1,13))
        Month.place(x=295,y=215)

        #l snen
        self.Year=StringVar(master=root)
        yearLabel=Label(root,text="Year").place(x=400,y=215)
        Year=ttk.Combobox(root,textvariable=self.Year,width=4)
        Year['values']=list(range(1970,2014))
        Year.place(x=430,y=215)




        #l madena
        self.Country=StringVar(master=root)
        country=ttk.Combobox(root,textvariable=self.Country,width=53)
        country['values']=('Ismailia',
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
        country.place(x=140,y=250)



        self.PhoneNum = StringVar(master=root)
        phoneNumberEntry = Entry(root, width=55, bd=4,textvariable=self.PhoneNum).place(x=140, y=290, height=30)

        w=Canvas(root,cursor='arrow',height=2,width=500).place(x=5,y=380)



        #lw String VAr ha3mlo get laken lw variable 3ady haktab asmo w 5las bass lazam 2apleh self bardo
        '''
        show=Button(root,text="show",command=lambda : prinNamme(self.username.get(),
                                                                self.Email.get(),
                                                                self.password.get(),
                                                                self.Day.get(),
                                                                self.Month.get(),
                                                                self.Year.get(),
                                                                self.PhoneNum.get()
                                                                )) #.place(x=260,y=400)

        '''

        havAccount=Button(root,text="I Have Account ..",command=lambda :haveAcc(root),padx=10,bd=5).place(x=20,y=420)
        loginnowbutton=Button(root,text='Login',command=lambda :loginNow(self.username.get(),
                                                                   self.Email.get(),
                                                                   self.password.get(),
                                                                   self.Day.get(),
                                                                   self.Month.get(),
                                                                   self.Year.get(),
                                                                   self.Country.get(),
                                                                   self.PhoneNum.get(),
                                                                    root
                                                                   )
                        ,padx=15,bd=5).place(x=400,y=420)

        root.deiconify()
        root.mainloop()

obj1=SignUp()