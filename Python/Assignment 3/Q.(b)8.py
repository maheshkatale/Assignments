"""
8) Note: use List comprehension
 create a list with the numbers from 1 to 20
 create one more list which should contain only odd numbers from the first list.
"""

List1= [i for i in range (1,21)]
print(List1)

List2= [i for i in range (1,21) if (i%2!=0)]
print(List2)
