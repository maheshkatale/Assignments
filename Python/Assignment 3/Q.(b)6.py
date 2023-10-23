"""
6) accept 5 numbers, store them inside the list. now accept a position from user ,remove the element from that position and  after removing it, display the list.
"""

List=[]
for i in range (5):
    num=int(input("Enter the number : "))
    List.append(num)

index=int(input("enter the index from where you want to remove the number : "))
List.pop(index)

print(List)
