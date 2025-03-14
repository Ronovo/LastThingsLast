import formatter
from Game.Logic import buildingHelper, timeHelper
import CharacterHelper

cabin = {
    "Entry" : {"Name": "Entry", "Rooms" : ["Cabin","Shed"]},
    "Cabin" : {"Name": "Cabin","Rooms" : ["Shed"], "Inspect" : ["Bed","Note"], "Actions" : ["Open Box"]},
    "Shed" : {"Name": "Shed","Rooms" : ["Cabin", "Outhouse","Septic Tank"], "Inspect" : ["Tools","Gas Cans"]},
    "Outhouse" : {"Name": "Outhouse","Rooms" : ["Cabin", "Shed","Septic Tank"], "Inspect" : ["Outhouse"]},
    "Septic Tank" : {"Name": "Septic Tank","Rooms" : ["Cabin", "Shed","Outhouse"], "Inspect" : ["Septic Tank"], "Actions" : ["Open Tank"]}
}

descriptionDictionary = {
    "Bed" : "Small cot, with pillows and blankets. Underneath is a lockbox with a green triangle on it.\nAlso a note?",
    "Tools" : "Various tools, and multiple tool benches.",
    "Gas Cans" : "2 x Five Gallon gas cans, completely full.",
    "Note" : "To Whom it may concern.\n"
             "If you are reading this note, I can assume I have died or become incapacitated in some way\n"
             "before I had the courage to complete my final mission. You will find about 10 gallons of gas\n"
             "in the shed behind the cabin. Pour it into the septic tank behind the cabin, and ignite it.\n"
             "You'd be happier if you didn't look inside. Please make sure the remains are kept from my children.\n"
             "-Clyde",
    "Outhouse" : "Someone used this recently. Why would someone use an outhouse if there is a septic tank?",
    "Septic Tank" : "Half buried septic tank. No pipes run to the cabin. Both entrances have padlocks on them."
}

def searchCabin(characterData):
    room = cabin["Entry"]
    while 1:
        formatter.clear()
        roomName = room["Name"]
        formatter.drawMenuLine()
        print("Room Name : " + roomName)
        match roomName:
            case "Cabin":
                print("The Kitchen is mostly bar, with a smattering of cans, pans, and empty boxes.")
                print("The only human touch is a drawing on the fridge.")
            case "Shed":
                print("A shed with tools and a few gas cans on the ground.")
            case "Septic Tank":
                print("You move towards the septic tank. It is very conspicuous.")
        result = choiceMenu(characterData, room)
        room = result[1]
        characterData = result[0]
        if characterData["Current Scene"] == 4:
            return characterData

def choiceMenu(characterData, room):
    formatter.drawMenuLine()
    print("Choices")
    formatter.drawMenuLine()
    print("1. Move to another room")
    print("2. Inspect this room")
    print("3. Actions in room")
    print("4. Get Current Time")
    print("5. Check Character Sheet")
    print("6. Quit (Progress saved at start of scene)")
    menuInput = input("Please select your answer...\n")
    try:
        menuNumber = int(menuInput)
        formatter.clear()
        match menuNumber:
            case 1:
                roomName = buildingHelper.moveRoom(room)
                room = cabin[roomName]
            case 2:
                buildingHelper.inspectRoom(room, descriptionDictionary)
            case 3:
                characterData = buildingHelper.actionsInRoom(room, characterData, 4)
            case 4:
                timeHelper.showTime(characterData)
                input("Press any key to continue...")
            case 5:
                loadedCharacter = CharacterHelper.getCharacterMenu()
                CharacterHelper.checkCharacterMenu(loadedCharacter)
            case 6:
                quit()
    except TypeError:
        input("Invalid Input. Press anything to try again...")
    result = [characterData, room]
    return result