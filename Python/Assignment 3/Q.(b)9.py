"""
9) accept 5 names and store them in list. Now sort the list in ascending order display and then in descending order.
"""

List=[]
for i in range (5):
    num=int(input("enter the number : "))
    List.append(num)
print("Before sorting:\t",List)

List.sort()
print("increasing order:\t",List)

List.sort(reverse=True)
print("decreasing order:\t",List)
