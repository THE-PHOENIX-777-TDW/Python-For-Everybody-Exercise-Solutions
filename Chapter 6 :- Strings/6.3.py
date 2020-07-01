def count(letter,string):
    count = 0
    for char in string:
        if (char == letter ):
            count = count + 1
    print(count)

seq=input("Enter the String : ")
let=input("Enter The Character You wish to search for : ")
count(let,seq)
