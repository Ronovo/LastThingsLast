def subtractTime(characterData, x):
    characterData["Hours Left"] -= x
    characterData["Time Until Sleep"] -= x
    return characterData

def showTime(characterData):
    hours = characterData["Hours Left"]
    date = "03/10/2010"
    passedHours = 48 - hours
    initialStartTime = 14 #2 PM in Military Time
    currentTime = initialStartTime + passedHours
    if currentTime >= 24:
        date = "03/11/2010"
        currentTime -= 24
    if currentTime < 12:
        suffix = " AM"
    else:
        currentTime -= 12
        suffix = " PM"
    print("Current Date : " + date)
    print("Current Time : " + str(currentTime) + suffix)
    print("Hours left in mission : " + str(characterData["Hours Left"]))
    print("Hours left until sleep: " + str(characterData["Time Until Sleep"]))

def checkSleep(characterData):
    hours = characterData["Hours Left"]
    date = "03/10/2010"
    passedHours = 48 - hours
    initialStartTime = 14  # 2 PM in Military Time
    currentTime = initialStartTime + passedHours
    if currentTime >= 24:
        date = "03/11/2010"
        currentTime -= 24
    if currentTime >= 18:
        return True
    else:
        return False

