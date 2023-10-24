"""
2) create a tuple to store 5 numbers and then sort it in ascending and descending order.
"""

tuple1= (4,6,7,3,9)

list1=list(tuple1)
list1.sort()
print("ascending order:\t",list1)

list1.sort(reverse=True)
print("descending order:\t",list1)
