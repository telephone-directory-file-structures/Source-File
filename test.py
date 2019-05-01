import re

#print(record)
def search(txt_file,idx_file,key):
	record=[]
	record=open(txt_file).readlines()
	print(record)
	flag=0
	idx_f=open(idx_file,"r")
	#print(idx_f)
	for line in idx_f:
		#print(line)
		if re.match(key,line):
			flag=1
			l=line.split()
			n=len(l)
			txt_f=open(txt_file,"r")
			for i in range (1,n):
				c=int(l[i])
				#print(record[c-1])
			#return l
				l2=record[c-1].split('|')
			print("\nFIR number:"+l2[0])
			print("Victim name:"+l2[1])
			print("Accused name:"+l2[2])
			print("Case date:"+l2[3])
			print("Case time:"+l2[4])
			print("Case description:"+l2[5])
			print("Case status:"+l2[6]+"\n")
			
			txt_f.close()
			
	if(flag==0):
			print("No such record exist")
	idx_f.close()

search("cdetail.txt","indexfile.txt","F15")
