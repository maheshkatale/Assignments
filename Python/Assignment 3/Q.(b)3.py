"""
3) accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at the end of the list using "extend" method.
"""

List=[]
for i in range(5):
    num=int(input("Enter the number = "))
    List.append(num)

List.extend([12,37,45])

print(List)
