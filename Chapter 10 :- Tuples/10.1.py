mail_dict=dict()
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        break
    except:
        print("No Such File or Directory")

for line in fhand:
    if(line.startswith("From")):
        words = line.split()
        if(len(words)>3):
            mail_dict[words[1]]=mail_dict.get(words[1],0)+1

Commit_lst=[]
for key,val in mail_dict.items():
    Commit_lst.append((val,key))
Commit_lst.sort(reverse=True) #Sort in Ascending Order
print(Commit_lst[0][1],Commit_lst[0][0])
