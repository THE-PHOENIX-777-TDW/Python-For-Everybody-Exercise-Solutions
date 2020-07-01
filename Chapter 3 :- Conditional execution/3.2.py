try:
    Hours=int(input("Enter Hours: "))
    Rate_Per_Hr=float(input("Enter Rate: "))


    #Checking if Hours are more than 40
    if(Hours>40):
        #Formula for Comupting 1.5 times the hourly rate for Hours worked.
        Pay=str((40*Rate_Per_Hr)+((Hours-40)*(Rate_Per_Hr*1.5)))
    else:
        Pay=str(Hours*Rate_Per_Hr)


    print("Pay: "+Pay)

except:
    print("Error, please enter numeric input")
