ch = ord(input("Enter the character : "))

if(ch>=ord('a') and ch<=ord('z')):
    print("Lower Case")
elif(ch>=ord('A') and ch<=ord('Z')):
    print("Upper Case")
else:
    print("Not an Alphabet")
