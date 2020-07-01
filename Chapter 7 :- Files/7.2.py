Total=0
Count=0
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file Location : ")
        file=open(file_loc,"r")

        for line in file:
            if(line.startswith("X-DSPAM-Confidence")):
                line=line.rstrip() #Strip any Spaces on Right
                ind=line.find(":")
                val=line[ind+1:]
                val=float(val.strip()) #Strip Space Before & After Number
                Total=Total+val #Accumulator Variable
                Count=Count+1
        print("Average spam confidence:",Total/Count)        
        break
    except:
        print("No Such File or Directory")
