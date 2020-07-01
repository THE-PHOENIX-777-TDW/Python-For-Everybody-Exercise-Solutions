import re

count=0
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        reg=input("Enter a regular expression : ")
        break
    except:
        print("No Such File or Directory")

for line in fhand:
    if re.search(reg,line):
        count+=1

directory=file_loc.split("\\")
file=directory[-1]
print("%s had %d lines that matched %s"%(file,count,reg))
