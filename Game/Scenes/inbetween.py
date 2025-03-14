import formatter
from Game.Logic import timeHelper, handler
from Game.Scenes import meeting


def inBetweenMenu(characterData):
    while 1:
        formatter.clear()
        formatter.drawMenuLine()
        print("Downtime Menu")
        formatter.drawMenuLine()
        print("1. Check Time")
        print("2. Go to Hotel")
        print("3. Go to Next Mission Location")
        print("4. Quit and Save Game")
        menuInput = input("Please select your answer...\n")
        check = menuInput.isnumeric()
        if check:
            menuNumber = int(menuInput)
            formatter.clear()
            match menuNumber:
                case 1:
                    timeHelper.showTime(characterData)
                    input("Press any key to continue...\n")
                case 2:
                    characterData = hotel(characterData)
                case 3:
                    characterData["Current Scene"] = characterData["Next Scene"]
                    characterData["Next Scene"] = 99
                    return characterData
                case 4:
                    quit()
                case _:
                    print("Not a valid option. Please try again!")


def sleep(characterData):
    while 1:
        formatter.clear()
        formatter.drawMenuLine()
        print("Sleep Menu")
        formatter.drawMenuLine()
        check = timeHelper.checkSleep(characterData)
        if check:
            print("1. Sleep for x hours")
        else:
            print("x. Too early to sleep")
        print("2. Nap for an hour (Chance to Oversleep)")
        print("3. Return to hotel menu")
        menuInput = input("Please select your answer...\n")
        check = menuInput.isnumeric()
        if check:
            menuNumber = int(menuInput)
            match menuNumber:
                case 1:
                    #Can I get sued for that variable name?
                    sleepNumber = input("How many hours do you want to sleep?\n")
                    sleepNumber = int(sleepNumber)
                    break
                case 2:
                    luckRoll = handler.luckRoll()
                    if luckRoll:
                        print("You sleep for an hour, and wake up feeling well rested.")
                        sleepNumber = 1
                    else:
                        print("You oversleep, and napped for 2 hours. You wake up feeling like Rip Van Winkle.")
                        sleepNumber = 2
                    break
                case 3:
                    return characterData
                case _:
                    print("Not a valid option. Please try again!")
                    input("Press any key to try again...")
    characterData = timeHelper.subtractTime(characterData, sleepNumber)
    characterData["Time Until Sleep"] = 12
    timeHelper.showTime(characterData)
    input("Press any key to continue...")
    return characterData

def hotel(characterData):
    while 1:
        formatter.clear()
        formatter.drawMenuLine()
        print("Welcome to the hotel.")
        formatter.drawMenuLine()
        print("1. Check Mission Information")
        print("2. Sleep")
        print("3. Return to last scene")
        menuInput = input("Please select your answer...\n")
        if menuInput.isnumeric():
            menuNumber = int(menuInput)
            formatter.clear()
            match menuNumber:
                case 1:
                   characterData = meeting.objectives(characterData)
                case 2:
                    characterData = sleep(characterData)
                case 3:
                    return characterData
                case _:
                    print("Not a valid option. Please try again!")
        else:
            print("Not a valid option. Please try again!")
