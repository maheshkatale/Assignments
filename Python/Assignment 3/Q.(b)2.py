"""
2) first create list empty. accept numbers till user enters 0 and store them inside the list. Print the list and its length.
"""

L=[]
while (True):
    num=int(input("Enter the number (enter 0 to exit) : "))
    if(num==0):
        break
    L.append(num)

print("list is :\t",L)
print("Length of list = ",len(L))
