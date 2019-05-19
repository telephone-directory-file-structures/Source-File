from tkinter import *
import sys,re
import os

hashval=""

record=[]
record=open("hashcontent.txt").readlines()
# print("hashcontentfile",record)

def printtext():
    global hashval
    global entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9
    global string
    txt_fil=open("hashcontent.txt","a")
    ssn = entry_1.get()
    fname = entry_2.get()
    lname = entry_3.get()
    ph = entry_4.get()
    email = entry_5.get()
    add = entry_6.get()
    website = entry_7.get()
    # uname = entry_8.get()
    # password = entry_9.get()
    entry=hashval+'|'+ssn+'|'+fname+'|'+lname+'|'+ph+'|'+email+'|'+add+'|'+website+'|'+'\n'
    txt_fil.write(entry)
    txt_fil.close()


# idx_file=open("indexfile.txt","r")
txt_fil="hashcontent.txt"

ssn = sys.argv[1]
fname=lname=add=ph=website=email=""
l=[]
flag=0
idx_f=open("indexfile.txt","r").readlines()
# print(idx_f)
for line in idx_f:
    print("index",line)
    if re.match(key,line):
        flag=1
        l=line.split()
        print("list",l)
        n=len(l)
        print("length of list after space",n)
        txt_f=open(txt_file,"r")
        for i in range (1,n):
            c=int(l[i])
            print("c value",c)
        l2=record[c-1].split('|')
        print("l2 value",l2)
        txt_f.close()
        n=int(l[1])

        l3=record[n-1].split('|')
        print("l3 value",l3 )
        #l3[1]=""
        # l3[6]="test1" ### Taking the input
        file1=open("hashcontent.txt","w")
        file_size=len(record)
        record2=[]
        for i in range(1,file_size+1):

            if(i!=n):
            	record2.append(record[i-1])
        # print("record 2 before writing",record2)
        file1.writelines(record2)
        file1.close()
        
        hashval = l3[0]
        ssn=l3[1]
        fname=l3[2]
        lname=l3[3]
        ph=l3[4]
        email=l3[5]
        add=l3[6]
        website=l3[7]


root = Tk()
root.geometry('500x900')
root.title("Add GUI")
root.configure(background='#e9e4e6')

label_0 = Label(root, text="Telephone Directory",width=20,font=("bold", 20), background='#e9e4e6')
label_0.place(x=80,y=53)

label_1 = Label(root, text="SSN",width=20,font=("bold", 10), background='#e9e4e6')
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.pack()
entry_1.insert(END,ssn)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="First Name",width=20,font=("bold", 10), background='#e9e4e6')
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.pack()
entry_2.insert(END,fname)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Last Name",width=20,font=("bold", 10), background='#e9e4e6')
label_3.place(x=80,y=240)

entry_3 = Entry(root)
entry_3.pack()
entry_3.insert(END,lname)
entry_3.place(x=240,y=240)

label_4 = Label(root, text="Phone No.",width=20,font=("bold", 10), background='#e9e4e6')
label_4.place(x=80,y=300)

entry_4 = Entry(root)
entry_4.pack()
entry_4.insert(END,ph)
entry_4.place(x=240,y=300)

label_5 = Label(root, text="Email ID",width=20,font=("bold", 10), background='#e9e4e6')
label_5.place(x=80,y=360)

entry_5 = Entry(root)
entry_5.pack()
entry_5.insert(END,email)
entry_5.place(x=240,y=360)

label_6 = Label(root, text="Address",width=20,font=("bold", 10), background='#e9e4e6')
label_6.place(x=80,y=420)

entry_6 = Entry(root)
entry_6.pack()
entry_6.insert(END,add)
entry_6.place(x=240,y=420)

label_7 = Label(root, text="Website",width=20,font=("bold", 10), background='#e9e4e6')
label_7.place(x=80,y=500)

entry_7 = Entry(root)
entry_7.pack()
entry_7.insert(END,website)
entry_7.place(x=240,y=500)


b = Button(root, text='Submit',width=20,height=2,bg='#3bb4c1',fg='white', command=printtext).place(x=180,y=650)
# Button(root,text='Quit',width=20,height=2,bg='#3bb4c1',fg='white', command=dest).place(x=180, y= 700)

root.mainloop()

