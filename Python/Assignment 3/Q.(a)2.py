"""
2) write a function to display "Hello World" using
	a) normal function
	b) lambda
"""

def disp():
    print("Hello World")

print("Using Normal function ")
disp()

print("Using lambda function ")
(lambda : print("Hello World"))()
