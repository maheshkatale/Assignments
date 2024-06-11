"""
5) define a function to accept a number. This function should return 1 if a number passed is more than 0
return -1 if a number passed is less than 0 , else it should return 0.
"""

def test():
    num=int(input("enter the number : "))
    if(num>0):
        return 1
    elif(num<0):
        return -1
    return 0
    
print(test())
