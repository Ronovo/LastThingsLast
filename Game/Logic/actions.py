import random

import formatter
from Game.Logic import timeHelper
from Game.Scenes import apartment


def roll(number):
    return random.randint(1, number)


def serveAction(name, characterData):
    match name:
        case "Search Closet":
            characterData = searchCloset(characterData)
        case "Check Couch":
            characterData = checkCouch(characterData)
        case "Eat Donuts":
            characterData = eatDonuts(characterData)
        case "Search Magazines":
            characterData = magazines(characterData)
        case "Search Bedroom":
            characterData = searchBedroom(characterData)
        case "Toss Bedroom":
            characterData = tossBedroom(characterData)
        case "Search Boxes":
            characterData = searchBoxes(characterData)
        case "Open Box":
            characterData = openBox(characterData)
        case "Open Tank":
            characterData = openTank(characterData)
    return characterData

def checkCouch(characterData):
    #Luck Roll
    couch = roll(100)
    if 1 <= couch < 26 :
        print("You find nothing")
    elif 26 <= couch < 85:
        print("You find some spare change, but nothing too fancy")
        characterData["Cash"] += .50
    elif 85 <= couch < 95:
        print("You find a dollar bill")
        characterData["Cash"] += 1.00
    elif couch >= 95:
        print("You found a 5 dollar bill")
        characterData["Cash"] += 5.00
    print("DEBUG : Player Cash now " + str(characterData["Cash"]))
    return characterData


def eatDonuts(characterData):
    print("These donunts are not good. Even if they are designed to last forever, these haven't.")
    donutInput = input("Press 1 to eat and test constitution. Any other key to return...\n")
    check = donutInput.isnumeric()
    if check:
        if int(donutInput) == 1:
            conCheck = roll(100)
            if conCheck < characterData["BaseStats"]["Con"]:
                print("You are lucky, and don't feel any effects.")
            else:
                print("Your gut bubbles as the donut eats at your system.")
                print("You knew better, but you still took a bite.")
                characterData["DerivedStats"]["HP"] -= 1
                print("DEBUG : HP is now " + str(characterData["DerivedStats"]["HP"]))
            return characterData
        print("You decide to not eat the donut.")
        return characterData

def magazines(characterData):
    input("Press any key to do a search check...\n")
    searchCheck = roll(100)
    if searchCheck <= characterData["Skills"]["Search"]:
        print("This man is meticulous, but on a crossword puzzle, you find an underlined word")
        print("'Cabin'")
        print("On this puzzle, it is the answer to 9 down. However, it is underlined on another page.")
        print("On that page, cabin is nowhere in the sea of words that are crossword answers.")
        print("No other words seem underlined. This rings odd to you.")
        print("You take note and move along.")
        #TODO DEV NOTE Add investigation notes to put info in
    else:
        print("Nothing seems out of place to you. This man was very through.")
        print("Every Reader's Digest in a stack is ordered by date.")
        print("The Sports Illustrated weren't as organized, with ones mentioning an Iowa team")
        print("and Swimsuit Issues swimming near the top.")
    return characterData

def searchCloset(characterData):
    searchCheck = roll(100)
    if searchCheck <= characterData["Skills"]["Search"]:
        print("You find a key with a green triangle tag on it.")
        print("You put it in your pocket for later.")
        characterData["Armor/Gear"].append("Triangle Key")
        a = len(characterData["Armor/Gear"]) - 1
        item = characterData["Armor/Gear"][a]
        print(item + " added to inventory.")
    else:
        print("You find nothing of interest.")
    return characterData

def searchBedroom(characterData):
    print("Based on the pictures, you can tell, Clyde definitely seems to be a family man.")
    print("Him and his late wife, Marlene, high school graduation pictures of his two children,")
    print("a few photos of a grandchild. This must be the infamous Cassie from the fridge.")
    formatter.drawMenuLine()
    print("A ceramic paperweight of a child's handprint lies beside it. Crudely painted on it:")
    print("**Cassie, Age 4**")
    print("Spot on.")
    return characterData


def tossBedroom(characterData):
    print("This is not a stealthy action. You will make noise, and it can take an hour or two.")
    print("You are about to tear this bedroom apart and put it back together after, exactly as it was.")
    bedroomInput = input("Press 1 to continue. Press any other key to cancel this action...\n")
    check = bedroomInput.isnumeric()
    if check:
        if int(bedroomInput) == 1:
            # roll search -20 (easier) - success - bag of teeth - occult roll - unnatural + 1
            '''
            searchCheck = roll(100)
            searchCheck -= 20
            if searchCheck < 0:
                searchCheck = 0
            if searchCheck <= characterData["Skills"]["Search"]:
            '''
            print("You find a mundane leather pouch stuffed between the bed and mattress pad. When you open it, it contains:")
            formatter.drawMenuLine()
            print("-Tuft of black hair(Unknown Animal)")
            print("-Teeth(Human, possibly infant)")
            print("-Colorful feathers(Unknown Bird)")
            formatter.drawMenuLine()
            print("Very odd. You make a note of it, and put the bag in your pocket.")
            characterData["Armor/Gear"].append("Bag of Remains")
            a = len(characterData["Armor/Gear"]) - 1
            item = characterData["Armor/Gear"][a]
            print(item + " added to inventory.")

            input("Press any key to continue...")
            # add hour to time
            luckCheck = roll(100)
            if luckCheck < 51:
                print("Some time passes as you tear apart the bedroom.")
                characterData = timeHelper.subtractTime(characterData, 1)
            else:
                print(
                    "Unluckily, it takes you longer to put the bedroom back together. You spend 2 hours instead of 1.")
                characterData = timeHelper.subtractTime(characterData, 2)
            input("Press any key to continue...")

            # Stealth Roll - if fail, trigger Janowitz
            stealthCheck = roll(100)
            if stealthCheck > characterData["Skills"]["Stealth"]:
                formatter.clear()
                characterData = apartment.oldLadyBedroom(characterData)
                formatter.clear()
            else:
                print("Either you didn't make enough noise, or no one was around to hear you. You search with no interruptions")
        else:
            print("You decide to not tear apart the bedroom.")
    else:
        print("You decide to not tear apart the bedroom.")
    return characterData

def searchBoxes(characterData):
    print("You are about to search through boxes. This will take some time.")
    while 1:
        print("Options:")
        print("1. Take half to hotel with you (6 Hours + 2 Hours for Transport")
        print("2. Go through all boxes - 12 Hours")
        boxInput = input("What do you want to do?\n")
        check = boxInput.isnumeric()
        if check:
            match int(boxInput):
                case 1:
                    print("You go to the hotel, and look at the files when you are there.")
                    characterData = timeHelper.subtractTime(characterData,8)
                    print("After 2 hours of moving boxes from the apartment to the hotel, you start looking through the documents.")
                    print("6 Hours later, you come back with nothing interesting.")
                    sleepNumber = input("How many hours to you want to sleep? (Default: 8)\n")
                    check = sleepNumber.isnumeric()
                    if check:
                        sleepNumber = int(sleepNumber)
                    else:
                        sleepNumber = 8
                    characterData = timeHelper.subtractTime(characterData, sleepNumber)
                    characterData["Time Until Sleep"] = 12
                    print("Time to wake up!")
                    input("Press any button to check the time!\n")
                    break
                case 2:
                    print("You start working on the boxes.")
                    timeleft = 12 - characterData["Time Until Sleep"]
                    characterData = timeHelper.subtractTime(characterData,characterData["Time Until Sleep"])
                    print("You stop working. Looking around, you think you still have " + str(timeleft) + " hours of work left.")
                    print("You crash at the hotel, and sleep for 10 hours, due to how exhausted you are.")
                    characterData["Time Until Sleep"] = 12
                    input("Press any key to check the time...\n")
                    timeHelper.showTime(characterData)
                    input("Press any key to go back and finish the job...\n")
                    characterData = timeHelper.subtractTime(characterData,timeleft)
                    break
    timeHelper.showTime(characterData)
    input("Press any key to continue...")
    print(
        "You find papers that show that Clyde had a cabin. They were hidden behind the stacks of paper boxes, in an old shoe box.")
    print(
        "Cash receipts, notebook to track payments, coordinates. Remembering the key board by the door, you go and look again.")
    print("You find a house key that looks different from the apartment key.")
    print("You hope this is the cabin key. If not, you might have to use your lockpick training.")
    characterData["Next Scene"] = 3
    characterData["Current Scene"] = 99
    return characterData

def openBox(characterData):
    print("DEBUG : CHECK KEY OR LOCKPICK")
    print("DEBUG : BOX OPEN")
    print("DEBUG : BOX CONTENTS GO HERE")
    return characterData

def openTank(characterData):
    print("As you approach the tank, you hear an old, creaky voice from inside.")
    print("'please......help me........'")
    print("The ghostly wails let loos again as you confirm it came from inside.")
    print("'please.....you have to help me...he has trapped me down here......'")
    characterData["Current Scene"] = 4
    return characterData