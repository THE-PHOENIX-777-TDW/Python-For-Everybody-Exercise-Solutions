#Chop function takes a list & modifies it Permanently
def chop (list1):
    if(len(list1)>2):
        del list1[0]
        del list1[-1]
        return None

#Middle function takes a list & creates a new List
#it doesn't affect the Original List
def middle (list1):
    if(len(list1)>2):
        list2=list1[1:-1]
        return list2
    else:
        return []

x1=["sxss","ee","12","rr"]
x2=["name","place","animal","thing"]
print(chop(x1))
print(x1)
print(middle(x2))
print(x2)
