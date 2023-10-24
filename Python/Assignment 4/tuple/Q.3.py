"""
3) Write a Python program to find the repeated items of a tuple.
"""

tuple1 = (1,5,2,3,4,6,4,2,1,5,2)
set1=set()
for i in tuple1:
    if(tuple1.count(i)>1):
        set1.add(i)
print(set1)
