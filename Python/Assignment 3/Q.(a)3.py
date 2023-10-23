"""
3) write a function with 2 arguments , second argument should be "default argument" and display them. Using
	a) normal function 
	b) lambda
"""

def disp(a,b=10):
    print("Using normal function ",a," ",b)

disp(4,2)

(lambda x,y=10:print("Using lambda function ",x," ",y))(4)
