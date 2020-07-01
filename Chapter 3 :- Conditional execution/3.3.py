try:
    Score=float(input("Enter score : "))
    if(Score >= 0.0 and Score <=1.0):
        if(Score >= 0.9):
            print("A")
        elif(Score >= 0.8):
            print("B")
        elif(Score >= 0.7):
            print("C")
        elif(Score >= 0.6):
            print("D")
        else:
            print("F")
    else:
        print("Bad score")
except:
    print("Bad score")
