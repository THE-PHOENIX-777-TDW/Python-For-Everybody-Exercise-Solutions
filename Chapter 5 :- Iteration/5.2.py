inp=None
Num_Str=" "

while inp!="done":
    try:
        inp=input("Enter a number : ")
        if(inp!="done"):
            val=int(inp)
            Num_Str=Num_Str+" "+str(val)    
    except:
        print("Invalid input")

Str_List=Num_Str.split() #Splitting string of numbers
Num_List=[int(i) for i in Str_List] #Creating a list of Numbers
print(Num_List)
print("Maximum : %d\nMinimum : %d"%(max(Num_List),min(Num_List)))
