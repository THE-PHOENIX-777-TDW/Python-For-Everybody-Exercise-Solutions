alpha_lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count=[0 for i in range(26)]
while True: #Loop Until File Name is Entered Correctly
    try:
        file_loc=input("Enter file : ")
        fhand=open(file_loc,"r")
        break
    except:
        print("No Such File or Directory")

for line in fhand:
    for char in line:
        char=char.lower()
        for alpha in range(26):
            if(char==alpha_lst[alpha]):
                count[alpha]+=1

for i in range(26):
    print(alpha_lst[i],count[i])
