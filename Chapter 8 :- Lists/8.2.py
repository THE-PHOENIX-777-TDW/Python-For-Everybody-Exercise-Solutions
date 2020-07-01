count = 0
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        for line in fhand: #Iterating through each line in file
            words = line.split()
            print(words)
            # print('Debug:', words)
            if len(words) == 0 : #Checks if line is Blank
                continue
            if words[0] != 'From:' or len(words)<=2: #Checks for lines<2 Words
                continue
            print(words[2])
        quit()
    except:
        print("No Such File or Directory")



    
