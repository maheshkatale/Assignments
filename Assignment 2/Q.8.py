"""
8) write a function to accept minimum 3 characters and maximum 5 characters. 
    [ use default arguments method ]
"""

def accept_str(str="Vita"):
    if(len(str)>=3 and len(str)<=5):
        print("String Accepted")
    else:
        print("String Rejected")

accept_str("Mahesh")
