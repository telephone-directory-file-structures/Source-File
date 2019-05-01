import re
import sys
listsecon=[]
secon="secondary.txt"

a = sys.argv[1]
b = sys.argv[2]
flag=0
listsecon=open(secon).readlines()
for ele in listsecon:

	if re.match(ele,a) and re.match(ele,b):
		flag=1
		res=ele.split("|")
		print(res[2])
if flag==0:
	print("key not found")		


#print(listsecon)