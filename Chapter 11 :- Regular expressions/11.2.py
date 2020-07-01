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
    extract=re.findall("^New.*:.([0-9]+)",line)
    if(len(extract)>0):
        Total=int(extract[0])+Total
        Count+=1
print(int(Total/Count))


