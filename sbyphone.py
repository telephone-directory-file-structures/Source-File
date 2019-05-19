import sys
import os
from tkinter import *
import textwrap


def printtext():
	global entry_1,entry_2
	phone = entry_1.get()
	entry_1.delete(first=0,last=100)
	# entry_2.delete(first=0,last=100)
	os.system("python3 seconph.py "+phone)


def dest():
	ahead.close()
	root.destroy()



# ahead = open("hashcontnet.txt","r")
ahead = open("hashcontent.txt","r")
root = Tk()
root.geometry('500x500')
root.title("Search By Phone")
root.configure(background='#e9e4e6')

label_0 = Label(root, text="Search By Phone Number",width=20,font=("bold", 20))
label_0.place(x=80,y=53)

label_1 = Label(root, text="Number: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.pack()
entry_1.focus_set()
entry_1.place(x=240,y=130)




b = Button(root, text='Search',width=20,bg='brown',fg='white', command=printtext).place(x=180,y=300)
Button(root, text='Quit',width=20,bg='red',fg='white',command=dest).place(x=180,y=340)

root.mainloop()
