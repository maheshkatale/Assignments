marks = int(input("Marks got in exam : "))
if(marks<=100 & marks>=90):
    print("Distinction")
elif(marks>=75):
    print("First class")
elif(marks>=60):
    print("Second class")
elif(marks>=40):
    print("Pass")
else:
    print("Fail")
