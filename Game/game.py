import formatter
from Game.Logic import timeHelper
from CharacterHelper import saveCharacterStatus
from Game.Logic import handler
from Game.Scenes import cabin, apartment, encounter, inbetween, meeting


def scene1(characterData):
    characterData = meeting.briefing(characterData)

    luckFlag = handler.luckRoll()
    if not luckFlag:
        timeHelper.subtractTime(characterData, 1)
        print("Unfortunately, someone left the lights on.")
        print("It takes an hour for you to get it running, after getting a jump off a mail truck.")
        input("Press any key to continue...")
    return characterData

def scene2(characterData):
    #Time moves on
    timeHelper.subtractTime(characterData, 1)
    formatter.drawMenuLine()
    print("SCENE 2")
    formatter.drawMenuLine()
    print("After an hour of talking to Hands, and finding your way around, You arrive at the apartment.")
    print("Baughman's address is an inconspicuous apartment building in a declining neighborhood.")
    print("The building is a jarring example of early 1960s design, blocky and drab.")
    #TODO DM NOTE Roll for stealth if low stealth. For now, no chance on entry
    print("No one takes notice of a lone agent entering the building.")
    #TODO DM NOTE Roll for chance door is unlocked already.
    print("You also have a key, so you are not suspicious. At least, not yet.")
    input("Press any key to enter the apartment...\n")

    #TODO Dev Note Add logic to build a building, and have the player explore
    print("The interior of Baughman's small apartment is spartan and grim.")
    print("Aside from a patina of cigarette smoke, there is scant evidence that anyone actually lived there.")

    characterData = apartment.searchApartment(characterData)
    return characterData

def scene3(characterData):
    print("You take the key you found at the apartment, and coordinates to the cabin.")
    print("It takes 3 hours to drive there.")
    print("DEBUG: No Time Changes Programmed Yet")
    print("You pull up to the front of the cabin. It looks abandoned.")
    input("Press any key to continue...")

    characterData = cabin.searchCabin(characterData)
    return characterData


def scene4(characterData):
    characterData = encounter.startEncounter(characterData)
    return characterData


def endGame(characterData):
    print("You have reached the end of Last Things Last V0.1")
    print("Thank you for playing. More to come soon.")
    print("Report any bugs or typos you found back to Ronovo!")
    print("***Have a Spooky Day***")
    input("Press any key to exit...")
    return


def startGame(characterData):
    formatter.clear()
    while 1:
        match characterData["Current Scene"]:
            #Initial Meeting
            case 1:
                characterData = scene1(characterData)
                #TODO DM NOTES Add luck roll for car to not start
            #Apartment
            case 2:
                characterData = scene2(characterData)
            #Cabin
            case 3:
                characterData = scene3(characterData)
            # Encounter
            case 4:
                characterData = scene4(characterData)
            #In Between Scene Menu
            case 99:
                characterData = inbetween.inBetweenMenu(characterData)
            #End Game
            case 0:
                endGame(characterData)
                return
        saveCharacterStatus(characterData)