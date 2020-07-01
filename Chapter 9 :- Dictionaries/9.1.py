word_dict=dict()
count=0
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        for line in fhand:
            words=line.split()
            for word in words:
                if word not in word_dict:
                    word_dict[word]=count
                    count+=1
        break
    except:
        print("No Such File or Directory")

print(word_dict)
