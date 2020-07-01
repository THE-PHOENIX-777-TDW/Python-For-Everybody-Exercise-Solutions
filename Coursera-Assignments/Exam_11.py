import re

Count=0
Total=0
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        break
    except:
        print("No Such File or Directory")

for line in fhand:
    line=line.rstrip()
    extract=re.findall("([0-9]+)",line)
    if(len(extract)>0):
        for i in range(len(extract)):
            Total=int(extract[i])+Total
            Count+=1
print("There are %d values with a sum=%d"%(Count,Total))
