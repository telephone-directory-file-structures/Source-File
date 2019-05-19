import re
import sys
import os
from tkinter import *
from itertools import islice
listsecon=[]
secon="indexfile.txt"

def dest():
	ahead.close()
	root.destroy()

a = sys.argv[1]
flag=0
listsecon=open(secon).readlines()
ahead = open("hashcontent.txt","r")
for ele in listsecon:

	if re.match(ele,a):
		flag=1
		res=ele.split("|")
		n=int(res[1].strip(" "))
		# os.system("python3 ")

 
with open('hashcontent.txt') as f:
    try:
        line = next(islice(f, n-1, n))
    except StopIteration:
        print('No Record Found')

print(line)
words =line.split("|")

if flag==0:
	print("key not found")		


root = Tk()
root.geometry('500x500')
root.title("Result")

label_0 = Label(root, text="Result",width=20,font=("bold", 20))
label_0.place(x=50,y=53)

label_1 = Label(root, text="SSN: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
label_2 = Label(root, text=words[1],width=20,font=("bold", 10))
label_2.place(x=200,y=130)

label_3 = Label(root, text="First Name: ",width=20,font=("bold", 10))
label_3.place(x=60,y=160)
label_4 = Label(root, text=words[2],width=20,font=("bold", 10))
label_4.place(x=200,y=160)

label_5 = Label(root, text="Last Name: ",width=20,font=("bold", 10))
label_5.place(x=60,y=190)
label_6 = Label(root, text=words[3],width=20,font=("bold", 10))
label_6.place(x=200,y=190)

label_7 = Label(root, text="Phone: ",width=20,font=("bold", 10))
label_7.place(x=60,y=220)
label_8 = Label(root, text=words[4],width=20,font=("bold", 10))
label_8.place(x=200,y=220)

label_9 = Label(root, text="Email ID: ",width=20,font=("bold", 10))
label_9.place(x=60,y=250)
label_10 = Label(root, text=words[5],width=20,font=("bold", 10))
label_10.place(x=200,y=250)

label_11 = Label(root, text="Address: ",width=20,font=("bold", 10))
label_11.place(x=60,y=280)
label_12 = Label(root, text=words[6],width=20,font=("bold", 10))
label_12.place(x=200,y=280)

label_13 = Label(root, text="webiste: ",width=20,font=("bold", 10))
label_13.place(x=60,y=310)
label_14 = Label(root, text=words[7],width=20,font=("bold", 10))
label_14.place(x=200,y=310)


# b = Button(root, text='Search by Name',width=20,bg='red',fg='white', command=searchn).place(x=150,y=370)
Button(root, text='Quit',width=20,bg='red',fg='white', command=dest).place(x=150,y=400)
# Button(root,text='Search by Phone Number',width=20,bg='red',fg='white',command=searchp).place(x=150,y=430)
root.mainloop()
