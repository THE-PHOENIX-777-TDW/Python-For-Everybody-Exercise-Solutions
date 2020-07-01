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
        if(len(words)>2):
            ind=words[1].find("@")
            key=words[1][ind+1:]
            mail_dict[key]=mail_dict.get(key,0)+1
print(mail_dict)
