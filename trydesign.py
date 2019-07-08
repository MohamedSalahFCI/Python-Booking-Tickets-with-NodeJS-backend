from tkinter import *


root = Tk()

#root.geometry("370x450")
'''
#simple
Label(root, text="Red Sun", bg="red", fg="white").pack()
Label(root, text="Green Grass", bg="green", fg="black").pack()
Label(root, text="Blue Sky", bg="blue", fg="white").pack()
'''
'''z
#fill option (X)
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X)

'''
'''
#padx 	External padding, horizontally
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X,padx=50)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X,padx=50)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,padx=50)
'''
'''
#pady 	External padding, vertically
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X,pady=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X,pady=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,pady=10)

'''
'''
#ipadx 	Internal padding, horizontally.
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipadx=30)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack()
'''
'''
#ipady 	Internal padding, vertically
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipadx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(ipady=10)
'''

'''
#placing Left
w = Label(root, text="red", bg="red", fg="white")
w.pack(padx=5, pady=50, side=LEFT)
w = Label(root, text="green", bg="green", fg="black")
w.pack(padx=5, pady=50, side=LEFT)
w = Label(root, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=50, side=LEFT)

#placing Right
w = Label(root, text="red", bg="red", fg="white")
w.pack(padx=5, pady=50, side=RIGHT)
w = Label(root, text="green", bg="green", fg="black")
w.pack(padx=5, pady=50, side=RIGHT)
w = Label(root, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=50, side=RIGHT)
'''
mainloop()