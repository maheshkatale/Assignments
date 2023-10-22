"""
3) define a function which accepts character,int,string and display them.
"""

ch=input("Enter the character : ")
num=int(input("Enter the number : "))
str=input("Enter the string : ")

def disp(char,number,string):
    print("Entered charcter number string is\n",char,"\t",number,"\t",string)
    
disp(ch,num,str)
