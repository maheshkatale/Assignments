ch = input("Enter the character : ")
match ch:
    case 'A'|'a'|'E'|'e'|'I'|'i'|'O'|'o'|'U'|'u':
        print("It is a vowel")
    case _ :
        print("It is not a vowel")
