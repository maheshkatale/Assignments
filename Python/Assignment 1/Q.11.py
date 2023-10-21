i = int(input("Enter the number : "))
for j in range (2,int(i/2+1)):
    if(i%j==0):
        print("It is not a prime number")
        break
else:
    print("It is a prime number")
