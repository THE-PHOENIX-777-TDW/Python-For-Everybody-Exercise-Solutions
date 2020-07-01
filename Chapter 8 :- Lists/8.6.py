num_lst=[]
inp=None
while True:
    try:
        inp=input("Enter a number : ")
        if(inp=="done"):
            print("Maximum:",max(num_lst))
            print("Minimum:",min(num_lst))
            break
        else:
            num_lst.append(float(inp))
    except:
        print("Enter valid Input")
