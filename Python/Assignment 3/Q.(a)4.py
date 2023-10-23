"""
4) write a function with variable no. of arguments and display them. Using
	a) normal function
	b) lambda
"""

def functn(*varg):
    for i in varg:
        print(i,end=" ")
print("Using normal function")
functn(10,2,4,9,5,6,7)

print("\nUsing lambda function")
(lambda *varg: [print(i,end=" ") for i in varg])(5,2,1,7,8,9)
