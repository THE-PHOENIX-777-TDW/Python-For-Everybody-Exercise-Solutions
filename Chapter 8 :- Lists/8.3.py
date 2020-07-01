while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        for line in fhand:
            words = line.split()
            print(words)
            # print('Debug:', words)
            if len(words) == 0  or words[0] != 'From:' or len(words)<=2:
                continue
            print(words[2])
        quit()
    except:
        print("No Such File or Directory")
