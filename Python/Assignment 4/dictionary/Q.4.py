"""
4)  Given a dictionary of students and their favourite colours: 
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
1. Find out how many students are in the list 
2. Change Lisa’s favourite colour 
3. Remove 'Jenny' and her favourite color
4. Sort and print students and their favourite colours alphabetically by name
"""

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print("Total number of entries : ",len(people))

people['Lisa'] = 'Red'
print(people)

people.pop('Jenny')
print(people)

ordered_list= sorted(people.items(), key=lambda x:x[0])
print("Alphabetically sorted list:\t",ordered_list)
