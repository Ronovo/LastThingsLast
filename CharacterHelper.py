import json
import os

import formatter

def checkCharacterMenu(character):
    while 1:
        formatter.clear()
        formatter.drawMenuLine()
        print("Character Menu")
        formatter.drawMenuLine()
        print("1. Basic Information")
        print("2. Base/Derived Stats")
        print("3. Skills")
        print("4. Additional Information")
        print("5. Quit")
        characterInput = input("Please select your answer...\n")
        try:
            formatter.clear()
            menuNumber = int(characterInput)
            match menuNumber:
                case 1:
                    print("Name : " + character['Real Name'])
                    print("Agent Name : " + character['Agent Name'])
                    print("Profession : " + character['Profession'])
                    print("Employer : " + character['Employer'])
                    print("Nationality : " + character['Nationality'])
                    print("DOB : " + character['DOB'])
                    print("Physical Description : " + character['Physical Description'])
                    formatter.drawMenuLine()
                    print("Education")
                    formatter.drawMenuLine()
                    for x in character["Education"]:
                        print("-" + x)
                    formatter.drawMenuLine()
                    print("Motivations")
                    formatter.drawMenuLine()
                    for x in character["Motivations"]:
                        print("-" + x)
                    formatter.drawMenuLine()
                    print("Bonds")
                    formatter.drawMenuLine()
                    for x in character["Bonds"].keys():
                        print("Bond Name : " + x)
                case 2:
                    formatter.drawMenuLine()
                    print("BASE STATS")
                    formatter.drawMenuLine()
                    print("Strength : " + str(character['BaseStats']['Str']))
                    print("Constitution : " + str(character['BaseStats']['Con']))
                    print("Dexterity : " + str(character['BaseStats']['Dex']))
                    print("Intelligence : " + str(character['BaseStats']['Int']))
                    print("Power : " + str(character['BaseStats']['Pow']))
                    print("Charisma : " + str(character['BaseStats']['Cha']))
                    formatter.drawMenuLine()
                    print("DERIVED STATS")
                    formatter.drawMenuLine()
                    print("Hit Points : " + str(character['DerivedStats']['HP']))
                    print("Willpower : " + str(character['DerivedStats']['WP']))
                    print("Remaining Sanity : " + str(character['DerivedStats']['San']))
                    print("Breaking Point : " + str(character['DerivedStats']['BP']))
                case 3:
                    formatter.drawMenuLine()
                    print("SKILLS")
                    formatter.drawMenuLine()
                    print("Accounting : " + str(character['Skills']['Accounting']))
                    print("Alertness : " + str(character['Skills']['Alertness']))
                    print("Anthropology : " + str(character['Skills']['Anthropology']))
                    print("Archaeology : " + str(character['Skills']['Archaeology']))
                    for key in character['Skills']['Art']:
                        print("Art (" + key + "): " + str(character['Skills']['Art'][key]))
                    print("Artillery : " + str(character['Skills']['Artillery']))
                    print("Athletics : " + str(character['Skills']['Athletics']))
                    print("Bureaucracy : " + str(character['Skills']['Bureaucracy']))
                    print("Computer Science : " + str(character['Skills']['Computer Science']))
                    for key in character['Skills']['Craft'].keys():
                        print("Craft (" + key + "): " + str(character['Skills']['Craft'][key]))
                    print("Criminology : " + str(character['Skills']['Criminology']))
                    print("Demolitions : " + str(character['Skills']['Demolitions']))
                    print("Disguise : " + str(character['Skills']['Disguise']))
                    print("Dodge : " + str(character['Skills']['Dodge']))
                    print("Drive : " + str(character['Skills']['Drive']))
                    print("Firearms : " + str(character['Skills']['Firearms']))
                    print("First Aid : " + str(character['Skills']['First Aid']))
                    print("Forensics : " + str(character['Skills']['Forensics']))
                    print("Heavy Machinery : " + str(character['Skills']['Heavy Machinery']))
                    print("Heavy Weapons : " + str(character['Skills']['Heavy Weapons']))
                    print("History : " + str(character['Skills']['History']))
                    print("HUMINT : " + str(character['Skills']['HUMINT']))
                    print("Law : " + str(character['Skills']['Law']))
                    print("Medicine : " + str(character['Skills']['Medicine']))
                    print("Melee Weapons : " + str(character['Skills']['Melee Weapons']))
                    for key in character['Skills']['Military Science']:
                        print("Military Science (" + key + "): " + str(character['Skills']['Military Science'][key]))
                    print("Navigate : " + str(character['Skills']['Navigate']))
                    print("Occult : " + str(character['Skills']['Occult']))
                    print("Persuade : " + str(character['Skills']['Persuade']))
                    print("Pharmacy : " + str(character['Skills']['Pharmacy']))
                    print("Pilot : " + str(character['Skills']['Pilot']))
                    print("Psychotherapy : " + str(character['Skills']['Psychotherapy']))
                    print("Ride : " + str(character['Skills']['Ride']))
                    for key in character['Skills']['Science']:
                        print("Science (" + key + "): " + str(character['Skills']['Science'][key]))
                    print("Search : " + str(character['Skills']['Search']))
                    print("SIGINT : " + str(character['Skills']['SIGINT']))
                    print("Stealth : " + str(character['Skills']['Stealth']))
                    print("Surgery : " + str(character['Skills']['Surgery']))
                    print("Survival : " + str(character['Skills']['Survival']))
                    print("Swim : " + str(character['Skills']['Swim']))
                    print("Unarmed Combat : " + str(character['Skills']['Unarmed Combat']))
                    print("Unnatural : " + str(character['Skills']['Unnatural']))
                    for key in character['Skills']['Language']:
                        print("Language (" + key + "): " + str(character['Skills']['Language'][key]))
                case 4:
                    print("Wounds and Ailments:")
                    print(character['Wounds'])
                    print("Armor and Gear:")
                    gearString = ""
                    for x in character['Armor/Gear']:
                        gearString = gearString + x + ","
                    gearString = gearString[:-1]
                    print(gearString)
                    print("Armor and Gear:")
                    weaponString = ""
                    for x in character['Weapons']:
                        weaponString = weaponString + x + ", "
                    weaponString = weaponString[:-1]
                    print(weaponString)
                    print("Personal Details: ")
                    print(character['Personal Details'])
                    print("Special Training:")
                    trainingString = ""
                    for x in character['Special Training']:
                        trainingString = trainingString + x + ", "
                    trainingString = trainingString[:-1]
                    print(trainingString)
                case 5:
                    return
            input("Press any Key To Continue...")

        except TypeError:
            input("Invalid Input. Press anything to try again...")


def createNewCharacter():
    with open("new.json", mode="r", encoding="utf-8") as read_file:
        newCharacterData = json.load(read_file)

    print("Welcome to the new character menu!")
    formatter.drawMenuLine()
    name = input("Please enter your character's first and last name\n")
    newCharacter = newCharacterData['New Character Template']
    newCharacter["Real Name"] = name
    fileName = "Characters/" + name + ".json"
    with open(fileName, mode="w", encoding="utf-8") as write_file:
        json.dump(newCharacter, write_file)

    print("Now it is time to pick your agent name. What codename would you like to be?")
    print("Examples would be : Agent Winters, Agent 47, Agent Red")
    agentName = input("Please enter your name, Agent ")
    newCharacter["Agent Name"] = "Agent " + agentName

    print("Finally, add a physical description.")
    description = input("Enter your text below.\n")
    newCharacter["Physical Description"] = description

    # Save Character
    fileName = "Characters/" + name + ".json"
    with open(fileName, mode="w", encoding="utf-8") as write_file:
        json.dump(newCharacter, write_file, indent=2)
    return newCharacter

def saveCharacterStatus(characterData):
    filename = "Characters/" + characterData["Real Name"] + ".json"
    with open(filename, mode="w", encoding="utf-8") as write_file:
        json.dump(characterData, write_file, indent=2)

def getCharacterMenu():
    cwd = os.getcwd()
    path = cwd + "/Characters"
    items = os.listdir(path)
    fileList = []
    for file in items:
        nameLength = len(file)
        cutoff = nameLength - 5
        file = file[0:cutoff]
        fileList.append(file)
    # Menu
    print("Character Menu")
    print("--------------")
    n = 1
    for option in fileList:
        print(str(n) + ".) " + option)
        n += 1
    print(str(n) + ".) Return to Main Menu\n")
    answer = input("Please choose an option\n")
    if int(answer) == n:
        return
    else:
        fileIndex = int(answer) - 1
        grabFile = fileList[fileIndex]
        newPath = path + '/' + grabFile + '.json'
        with open(newPath, mode="r", encoding="utf-8") as read_file:
            newCharacterData = json.load(read_file)
            return newCharacterData