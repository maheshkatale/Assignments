"""
1) write a function to accept a number and return its square using
	a) normal function
	b) lambda
"""

def sqr(num):
    return num**2

num=int(input("Enter the number : "))
print("Using normal function : Square is",sqr(num))

print("Using lambda function : Square is",(lambda x:x**2)(num))
