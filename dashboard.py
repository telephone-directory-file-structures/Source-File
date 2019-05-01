import sys
import os
from tkinter import *	
import textwrap

def searchn():
	os.system("python3 sbyname.py")
def searchp():
	pass

def dest():
	ahead.close()
	root.destroy()

ssn = sys.argv[1]
fname = sys.argv[2]
lname = sys.argv[3]
ph = sys.argv[4]
email = sys.argv[5]
address = sys.argv[6]
website = sys.argv[7]
# ssn = 123

ahead = open("hashcontent.txt","r")
root = Tk()
root.geometry('500x500')
root.title("Dashboard")

label_0 = Label(root, text="Dashboard",width=20,font=("bold", 20))
label_0.place(x=50,y=53)

label_1 = Label(root, text="SSN: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
label_2 = Label(root, text=ssn,width=20,font=("bold", 10))
label_2.place(x=200,y=130)

label_3 = Label(root, text="First Name: ",width=20,font=("bold", 10))
label_3.place(x=60,y=160)
label_4 = Label(root, text=fname,width=20,font=("bold", 10))
label_4.place(x=200,y=160)

label_5 = Label(root, text="Last Name: ",width=20,font=("bold", 10))
label_5.place(x=60,y=190)
label_6 = Label(root, text=lname,width=20,font=("bold", 10))
label_6.place(x=200,y=190)

label_7 = Label(root, text="Phone: ",width=20,font=("bold", 10))
label_7.place(x=60,y=220)
label_8 = Label(root, text=ph,width=20,font=("bold", 10))
label_8.place(x=200,y=220)

label_9 = Label(root, text="Email ID: ",width=20,font=("bold", 10))
label_9.place(x=60,y=250)
label_10 = Label(root, text=email,width=20,font=("bold", 10))
label_10.place(x=200,y=250)

label_11 = Label(root, text="Address: ",width=20,font=("bold", 10))
label_11.place(x=60,y=280)
label_12 = Label(root, text=address,width=20,font=("bold", 10))
label_12.place(x=200,y=280)

label_13 = Label(root, text="webiste: ",width=20,font=("bold", 10))
label_13.place(x=60,y=310)
label_14 = Label(root, text=website,width=20,font=("bold", 10))
label_14.place(x=200,y=310)




b = Button(root, text='Search by Name',width=20,bg='red',fg='white', command=searchn).place(x=150,y=370)
Button(root, text='Quit',width=20,bg='red',fg='white', command=dest).place(x=150,y=400)
Button(root,text='Search by Phone Number',width=20,bg='red',fg='white',command=searchp).place(x=150,y=430)
root.mainloop()
