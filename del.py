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
    
    string += '\n\n1To see any of the below:\n'
    string += '1. View all Schools \n'
    string += '2. View all Divisions \n'
    
    
    
    
    answer = input ("Any more schools? ")
    if answer == "N":
        notDone = False
        #print(line)
        #print(aList)
        print(allCharacter)
    else:
        print("Let's add some more! ")
        
f.close()

##### use list commands like .append and a = aList and such. ask for help if cant remember