"""
7) create a list and store string,number,character,boolean,decimal values respectively inside it.
Now slice it in following ways:
a) display it in reverse order
b) list all the elements from 2nd position
c) list the elements from 1st to 3rd position
d) slice it from 1st to 3rd elements from the end.
"""

str=input("Enter the string : ")
num=int(input("Enter the number : "))
char=input("Enter the character : ")
bool_val=bool(input("Enter the Boolean value : "))
dec_val=float(input("Enter the decimal value : "))

List=[str, num, char, bool_val, dec_val]

print("reverse order:\t",List[::-1])

print("from 2nd positon:\t",List[2:])

print("from 1st to 3rd position:\t",List[1:4])

print("slice 1st to 3rd from the end:\t",List[-3:-1])
