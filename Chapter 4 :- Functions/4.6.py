def computepay(Hours,Rate_Per_Hr):
    #Checking if Hours are more than 40
    if(Hours>40):
        #Formula for Comupting 1.5 times the hourly rate for Hours worked.
        Pay=str((40*Rate_Per_Hr)+((Hours-40)*(Rate_Per_Hr*1.5)))
    else:
        Pay=str(Hours*Rate_Per_Hr)

    return Pay
    

try:
    Hrs=int(input("Enter Hours: "))
    Rate=float(input("Enter Rate: "))
    
    print("Pay:",computepay(Hrs,Rate))
except:
    print("Error, please enter numeric input")
