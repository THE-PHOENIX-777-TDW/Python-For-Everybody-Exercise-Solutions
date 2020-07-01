while True:
    try:
        file_loc=input("Enter file Location : ")
        file=open(file_loc,"r")

        for line in file:
            line=line.rstrip()
            print(line.upper())
        break
    except:
        print("No Such File or Directory")
