"""
9) define a function in such a way that it can accept n number of values and print their sum.
"""

def summation (*numbers):
    Sum=0
    for i in numbers:
        Sum+=i
    return Sum

print(summation(10,20,30,40))
