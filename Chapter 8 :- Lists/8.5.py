count = 0
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        for line in fhand:
            if(line.startswith("From:")):
                words = line.split()
                print(words[1])
                count+=1
        print("There were %d lines in the file with From as the first word"%(count))
        quit()
    except:
        print("No Such File or Directory")

