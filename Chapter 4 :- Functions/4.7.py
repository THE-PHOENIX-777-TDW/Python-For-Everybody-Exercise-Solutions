def computegrade(Grd):
    if(Score >= 0.0 and Score <=1.0):
        if(Score >= 0.9):
            return("A")
        elif(Score >= 0.8):
            return("B")
        elif(Score >= 0.7):
            return("C")
        elif(Score >= 0.6):
            return("D")
        else:
            return("F")
    else:
        return("Bad score")

try:
    Score=float(input("Enter score : "))
    print(computegrade(Score))
except:
    print("Bad score")
