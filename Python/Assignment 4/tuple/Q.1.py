1) Write a Python program to count the elements in a list until an element is a tuple.

Sample input : list = [10, 20, 30, (40,50), 60]
Sample output = 3

list = [10, 20, 30, (40, 50), 60]

cnt=0
for i in range (len(list)):
    if(type(list[i])==tuple):
        break
    cnt+=1

print(cnt)
