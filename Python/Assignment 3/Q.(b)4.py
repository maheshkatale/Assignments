"""
4) accept a number,string,decimal,boolean value and a character from the user and store it inside the list.
First print the list from the beginning and then from the end.
"""

num=int(input("Enter the number : "))
str=input("Enter the string : ")
dec=float(input("Enter the decimal value : "))
bool_val=bool(input("Enter the boolean value : "))
char=input("Enter the character : ")

List=[num, str, dec, bool_val, char]

print("from beginning:\t",List[:])
print("from end:\t",List[::-1])
