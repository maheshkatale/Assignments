"""
7) define a function which accepts a string , toggle and return it.
	[ hint :  use "swapcase()" function of string ]
"""

def swap(str):
    new_str=str.swapcase()
    return new_str

str=input("Enter the string : ")
print(swap(str))
