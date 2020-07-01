inp=None
Total=0
Count=0
while inp!="done":
    inp=input("Enter a number : ")
    try:
        if(inp!="done"):
            val=float(inp)
            Total=Total+val #Accumulator Variable
            Count=Count+1 #Keeping Track of Numbers Entered
    except:
        print("Invalid input")

print(Total,Count,Total/Count)
