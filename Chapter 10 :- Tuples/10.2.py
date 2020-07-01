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
        if(len(words)>=5):
            time_split=words[5].split(":")
            mail_dict[time_split[0]]=mail_dict.get(time_split[0],0)+1

Commit_lst=[]
for key,val in mail_dict.items():
    Commit_lst.append((key,val))
Commit_lst.sort()
for values in Commit_lst:
    print(values[0],values[1])
