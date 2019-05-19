import sys
import os
from tkinter import *
import textwrap


def printtext():
	global entry_1,entry_2
	fname = entry_1.get()
	lname = entry_2.get()
	entry_1.delete(first=0,last=100)
	entry_2.delete(first=0,last=100)
	os.system("python3 secon.py "+fname+" "+lname)


def dest():
	ahead.close()
	root.destroy()



# ahead = open("hashcontnet.txt","r")
ahead = open("hashcontent.txt","r")
root = Tk()
root.geometry('500x500')
root.title("Search by Name GUI")
root.configure(background='#e9e4e6')

label_0 = Label(root, text="Search By Name",width=20,font=("bold", 20),background='#e9e4e6')
label_0.place(x=80,y=53)

label_1 = Label(root, text="First Name",width=20,font=("bold", 10),background='#e9e4e6')
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.pack()
entry_1.focus_set()
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Second Name",width=20,font=("bold", 10),background='#e9e4e6')
label_2.place(x=80,y=160)

entry_2 = Entry(root)
entry_2.pack()
entry_2.focus_set()
entry_2.place(x=240,y=160)



b = Button(root, text='Search',width=20,height=2,bg='#3bb4c1',fg='white', command=printtext).place(x=180,y=300)
Button(root, text='Quit',width=20,height=2,bg='#3bb4c1',fg='white',command=dest).place(x=180,y=340)

root.mainloop()
