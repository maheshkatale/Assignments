a=0
b=1
summation=1
for i in range (8):
    sum=a+b
    a=b
    b=sum
    summation+=sum
print("Sum of first 10 fibonacci numbers = ",summation)
