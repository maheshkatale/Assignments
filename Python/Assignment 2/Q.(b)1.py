"""
1) create 3 functions "show1()","show2()" and "show3()"
now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.
invoke caller function by passing show1,show2 and show3
"""

def show1():
    print("in show1")
    
def show2():
    print("in show2")

def show3():
    print("in show3")
    
def caller(funtn):
    funtn()
    
caller(show2)
