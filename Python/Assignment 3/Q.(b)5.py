"""
5) accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove from the list and  after removing it, display the list.
"""

List=[]
i=5
while(i>0):
    num=int(input("Enter the number : "))
    List.append(num)
    i-=1

num=int(input("Which number you want to remove : "))
List.remove(num)

print(List)
