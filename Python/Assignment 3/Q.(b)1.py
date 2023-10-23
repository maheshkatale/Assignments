"""
1) create a list , accept a number,name and a float value from user and store it inside the list.
now accept one more name from user and insert it at 2nd position.
accept a number and append it at the end of the list. print the entire list.
"""

number1=int(input("Enter the number : "))
name1=input("Enter the name : ")
float_val1=float(input("Enter non-integer value : "))

L=[number1,name1,float_val1]

name2=input("Enter the name : ")
L.insert(2,name2)

number2=int(input("Enter the number : "))
L.append(number2)

print(L)
