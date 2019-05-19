from tkinter import *
import os
root = Tk()
root.geometry('500x300')
root.title("Login / Sign-up")

root.configure(background='#e9e4e6')

def dest():
	root.destroy()

def log():
	root.withdraw()
	os.system("python3 Logingui.py")
	root.update()
	root.deiconify()

def sin():
	root.withdraw()
	os.system("python3 AddguiT.py")
	root.update()
	root.deiconify()

label_0 = Label(root, text="Login / Sign-up",width=20,font=("bold", 20), background='#e9e4e6')
label_0.place(x=50,y=53)


b1 = Button(root, text='Login',width=20,bg='#3bb4c1',fg='white', command=log, height=2).place(x=150,y=100)
# b1.configure( height = 20, width = 40) 
Button(root, text='Sign-up',width=20,bg='#3bb4c1',fg='white', command=sin, height=2).place(x=150,y=150)
Button(root,text='Quit',width=20,bg='#3bb4c1',fg='white',command=dest, height=2).place(x=150,y=200)
root.mainloop()	