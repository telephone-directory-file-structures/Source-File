import re
import sys
import os
listsecon=[]
secon="secondaryph.txt"

a = sys.argv[1]

flag=0
listsecon=open(secon).readlines()
for ele in listsecon:

	if re.match(ele,a):
		flag=1
		res=ele.split("|")
		print(res[1])
		os.system("python3 prime.py "+res[1])
if flag==0:
	print("key not found")		
