def menu2():
    global notDone
    string =  ''
    string += '\n\nTo see any of the below:\n'
    string += '1. View all Schools \n'
    string += '2. View all Divisions \n'
    print(string)
    choice = input('Enter 1 or 2\n ')
    if choice == '1':
        print(school)
    elif choice == '2':
        print(division)


f = open("Schools.txt","a")
e = "Easy"
j = "Medium"
g = "Very"

notDone = True

allCharacter = []
while notDone:
    aList =[]
    school = input("School: ")
    f.write(school)
    f.write(" ")
    aList.append(school)
    division = input ("Division: ")
    aList.append(division)
    f.write(division)
    f.write(" ")
    print ("Challenge to get in: ")
    print(f'{e}\n{j}\n{g}')
    challenge = input (":")
    aList.append(challenge)
    f.write(challenge)
    f.write("\n")
    allCharacter.append(aList)
   

    
    
    
    answer = input ("Any more schools? ")
    if answer == "N":
        notDone = False
        #print(line)
        #print(aList)
        print(allCharacter)
    else:
        print("Let's add some more! ")
        
f.close()
notDone = True
while notDone:
    menu2()


##### use list commands like .append and a = aList and such. ask for help if cant remember