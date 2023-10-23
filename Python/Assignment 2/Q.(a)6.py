"""
6) define a function which accepts a character and return toggle of it. 
"""

def toggle(ch):
    if(ord(ch)>=65 and ord(ch)<=90):
        print(chr(ord(ch)+32))
    elif(ord(ch)>=97 and ord(ch)<=122):
        print(chr(ord(ch)-32))
    else:
        print("Invalid input")

ch=input("Enter the character : ")
toggle(ch)
