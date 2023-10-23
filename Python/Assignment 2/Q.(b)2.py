"""
2) define nested function and show how will you invoke it.
"""

def disp1():
    def disp2():
        print("in disp2")
    print("in disp1")
    return disp2

disp1()()
