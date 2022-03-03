

notDone = True

allCharacter = []
while notDone:
    aList =[]
    book = input("Book: ")
    aList.append(book)
    page = input ("Page Count: ")
    aList.append(page)
    year = int(input("Release Year: "))
    aList.append(year)
    allCharacter.append(aList)

    answer = input ("Are you done adding books? ")
    line = "\n\n**************************************\n"
    line += f"Years Since: {2022 - year}\n"
    line += "**************************************\n"
    if answer == "Y":
        notDone = False
        print(line)
        print(aList)
        print(allCharacter)
    else:
        print("Let's try again 😎. ")

##create larger list/inv and add smaller list to it. After that I should be done requirements
