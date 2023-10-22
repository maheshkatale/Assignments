"""
1) define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]
"""

def add():
    print("adding")

def modify():
    print("modifying")
    
def delete():
    print("deleting")
    
num=int(input("Choose the operation : "))
    
match (num):
    case 1:
        add()
    case 2:
        print()
    case 3:
        modify()
    case _:
        print("invalid input")
