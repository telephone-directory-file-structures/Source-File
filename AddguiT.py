import sys
import os
import textwrap
from tkinter import *

def printtext():
	global entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9
	global string
	ssn = entry_1.get()
	fname = entry_2.get()
	lname = entry_3.get()
	ph = entry_4.get()
	email = entry_5.get()
	add = entry_6.get()
	website = entry_7.get()
	uname = entry_8.get()
	password = entry_9.get()
	entry_1.delete(first=0,last=100)
	entry_2.delete(first=0,last=100)
	entry_3.delete(first=0,last=100)
	entry_4.delete(first=0,last=100)
	entry_5.delete(first=0,last=100)
	entry_6.delete(first=0,last=100)
	entry_7.delete(first=0,last=100)
	entry_8.delete(first=0,last=100)
	entry_9.delete(first=0,last=100)
	string_d = ssn+"|"+fname+"|"+lname+"|"+ph+"|"+email+"|"+add+"|"+website
	string_a = uname+"|"+password
	string_b = string_d+"|"+string_a+"\n"
	string_sn = fname+"|"+lname+"|"+ssn+"\n"
	print(string_sn)
	shead.write(string_sn)
	bhead.write(string_b)
	# print(string)
	# ahead.write(string)
	string_a= (''.join(format(ord(x), 'b') for x in string_a))
	# print("binary one",string)
	hashval = hashrec(string_a)
	string = hashval+"|"+string_d+"\n"
	ahead.write(string)

def dest():
	ahead.close()
	bhead.close()
	root.destroy()


def wordret(wa,wb,wc):
	a=int(wa,2)^int(wb,2)^int(wc,2)
	return '{0:032b}'.format(a)

def F1(S2,S3,S4):
	return (S2&S3)|(~S2&S4)
def F2(S2,S3,S4):
	return S2^S3^S4
def F3(S2,S3,S4):
	return (S2&S3)|(S2&S4)|(S3&S4)
def F4(S2,S3,S4):
	return S2^S3^S4

def process(chunk):
	words=[]
	# print(chunk)
	words=textwrap.wrap(chunk, 32)
	# print(words)
	# for i in range(0,3):
	words.append(wordret(words[0],words[1],words[2]))
	return words
	
def compress(words):
	k1=0x5A827999
	k2=0x6ED9EBA1
	k3=0x8F1BBCDC
	k4=0xCA62C1D6
	s1 = 0x67452301
	s2 = 0xEFCDAB89
	s3 = 0x98BADCFE
	s4 = 0x10325476
	s5 = 0xC3D2E1F0
	h1=s1
	h2=s2
	h3=s3
	h4=s4
	h5=s5
	for i in range(0,3):
		temp=s5+(s1<<5)+F1(s2,s3,s4)+k1+int(words[i],2)
		s5=s4
		s4=s3
		s3=s2
		s2=s1
		s1=temp
	h1 = h1 + s1 & 0xffffffff

	return h1


def hashrec(string):
	length=len(string)
	# print(string)
	low=0
	high=20
	# print("enter the hashrec")
	# print("lenght 1 : ",length)
	while(length>20):
		chunk=string[low:high]
		binlength='{0:064b}'.format(20)
		chunk+=binlength
		obj1=process(chunk)
		length=length-20
		low=low+20
		high=high+20
		obj2=compress(obj1)
		print("inside while")

	if(length==20):
		print("testing inside 20")
		string+='1'
		#append length
		length='{0:064b}'.format(length)
		string+=length
		obj1=process(string)
		obj2=compress(obj1)
	elif(length<20):
		#string='{0:b}'.format(ord(x) for x in message
		string+='1'
		length=len(string)
		for i in range(length,20):
			string+='0'
		#append length
		length='{0:064b}'.format(length)
		# print("lenght 2 :",length)
		# print("str",string)
		string+=length
		#print(string)
		#print(len(string))
		obj1=process(string)
		obj2=compress(obj1)
		# print("obj2",obj2)
	hand=open('hashcontent.txt','a')
	#hand.write('%08x%08x%08x%08x%08x' % (obj2[0],obj2[1],obj2[2],obj2[3],obj2[4])+" "+string+"\n")
	# print("String last :",string)

	# hand.write('%08x' % (obj2)+" "+string+"\n")
	# hand.write('%08x' % (obj2)+" "+"\n")
	return('%08x' % (obj2))
	#print('%08x%08x%08x%08x%08x' % (obj2[0],obj2[1],obj2[2],obj2[3],obj2[4]))
	# os.system('python3 indexing.py datafile.txt')


# string="karthikeya_gs_sanjay_das|sanjaydas"
# string=(''.join(format(ord(x), 'b') for x in string))
# hashrec(string)
ahead = open("hashcontent.txt","a+")
bhead = open("cdetail.txt","a+")
shead = open("secondary.txt","a+")

# MAIN STARTS HERE
root = Tk()
root.geometry('500x900')
root.title("Add GUI")

label_0 = Label(root, text="Telephone Directory",width=20,font=("bold", 20))
label_0.place(x=80,y=53)

label_1 = Label(root, text="SSN",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.pack()
entry_1.focus_set()
entry_1.place(x=240,y=130)

label_2 = Label(root, text="First Name",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.pack()
entry_2.focus_set()
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Last Name",width=20,font=("bold", 10))
label_3.place(x=80,y=240)

entry_3 = Entry(root)
entry_3.pack()
entry_3.focus_set()
entry_3.place(x=240,y=240)

label_4 = Label(root, text="Phone No.",width=20,font=("bold", 10))
label_4.place(x=80,y=300)

entry_4 = Entry(root)
entry_4.pack()
entry_4.focus_set()
entry_4.place(x=240,y=300)

label_5 = Label(root, text="Email ID",width=20,font=("bold", 10))
label_5.place(x=80,y=360)

entry_5 = Entry(root)
entry_5.pack()
entry_5.focus_set()
entry_5.place(x=240,y=360)

label_6 = Label(root, text="Address",width=20,font=("bold", 10))
label_6.place(x=80,y=420)

entry_6 = Entry(root)
entry_6.pack()
entry_6.focus_set()
entry_6.place(x=240,y=420)

label_7 = Label(root, text="Website",width=20,font=("bold", 10))
label_7.place(x=80,y=500)

entry_7 = Entry(root)
entry_7.pack()
entry_7.focus_set()
entry_7.place(x=240,y=500)

label_8 = Label(root, text="Username",width=20,font=("bold", 10))
label_8.place(x=80,y=560)

entry_8 = Entry(root)
entry_8.pack()
entry_8.focus_set()
entry_8.place(x=240,y=560)

label_9 = Label(root, text="Password",width=20,font=("bold", 10))
label_9.place(x=80,y=620)

entry_9 = Entry(root)
entry_9.pack()
entry_9.focus_set()
entry_9.place(x=240,y=620)


b = Button(root, text='Submit',width=20,bg='red',fg='white', command=printtext).place(x=180,y=650)
Button(root,text='Quit',width=20,bg='red',fg='white', command=dest).place(x=180, y= 700)

root.mainloop()
