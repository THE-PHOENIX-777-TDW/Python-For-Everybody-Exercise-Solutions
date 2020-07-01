words_lst=[]
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        for line in fhand:
            words = line.split()
            for word in words:
                if word not in words_lst: #check if word exist in list
                    words_lst.append(word) #if not then append
        words_lst.sort()
        print(words_lst)
    except:
        print("No Such File or Directory")

