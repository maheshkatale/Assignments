'''
1) Accept a number from the user check if it is special 
 * number or not? 
Example: 145
1! =1 
4!=1*2*3*4 
5!=1*2*3*4*5 
Sum of the factorials is (1+24+120=145) 

some other special numbers are 1,2 and 40585
'''

def fact(n):                    # Funtion to find factorial of digit
    if n==0:
        return 1
    result=1
    for i in range(n,1,-1):
        result*=i
    return result

def is_special(num):           # Function to check given number is special or not, returns true or false
    digits=str(num)
    fact_sum=0
    for digit in digits:
        fact_sum+=fact(int(digit))
    return fact_sum==num

number = int(input("Enter the number: "))
print(f"{number} is special number.") if is_special(number) else print(f"{number} is not a special number")
