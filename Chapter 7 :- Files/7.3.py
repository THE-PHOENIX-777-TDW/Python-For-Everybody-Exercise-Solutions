Total=0
Count=0
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        file=open(file_loc,"r")
        if(file_loc=="na na boo boo"): #Easter Egg Condition
            print("Boo Boo Who's There")

        for line in file:
            if(line.startswith("X-DSPAM-Confidence")):
                line=line.rstrip() #Strip any Spaces
                ind=line.find(":")
                val=line[ind+1:]
                val=float(val.strip()) #Strip Space Before & After Float
                Total=Total+val
                Count=Count+1
        print("Average spam confidence:",Total/Count)        
        break
    except:
        print("No Such File or Directory")

