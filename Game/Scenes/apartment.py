import formatter
from Game.Logic import handler, buildingHelper, timeHelper
import CharacterHelper

apartment = {
    "Entry" : {"Name": "Entry", "Rooms" : ["Kitchen","Living Room"], "Inspect" : ["Key Board w/ Hooks"]},
    "Kitchen" : {"Name": "Kitchen","Rooms" : ["Entry"], "Inspect" : ["Fridge"]},
    "Living Room" : {"Name": "Living Room","Rooms" : ["Entry", "Hallway"], "Inspect" : ["Magazines","Box of Donuts","Couch"], "Actions" : ["Check Couch","Eat Donuts","Search Magazines"]},
    "Hallway" : {"Name": "Hallway","Rooms" : ["Main Bedroom","Bathroom","Linen Closet","Bedroom"]},
    "Bathroom" : {"Name": "Bathroom","Rooms" : ["Hallway"]},
    "Linen Closet" : {"Name": "Linen Closet","Rooms" : ["Hallway"], "Actions" : ["Search Closet"]},
    "Main Bedroom" : {"Name": "Main Bedroom","Rooms" : ["Hallway"], "Actions" : ["Search Bedroom","Toss Bedroom"]},
    "Bedroom" : {"Name": "Bedroom","Rooms" : ["Hallway"], "Actions" : ["Search Boxes"]}
}

descriptionDictionary = {
    "Key Board w/ Hooks" : "Assorted Keys hang. Car key, copies of apartment keys, small keys. Nothing stands out",
    "Fridge" : "Hanging on the fridge is a drawing with two gold stars.\nIt depicts a crudely drawn stick figure named 'Granpa'.\nIt is signed 'Cassie'",
    "Couch" : "Relatively clean, smells like cigarettes. No change in between the cushions.",
    "Box of Donuts" : "A box of unhealthily artificial donuts, now crumbling and dry.",
    "Magazines" : "Mostly completed crossword puzzle books joining stacks of Sports Illustrated and Reader's Digest."
}

def searchApartment(characterData):
    startingRoom = apartment["Entry"]
    print("As you enter, you see there is a kitchen and a living room.")
    print("There is also a key board with hooks on the wall.")
    result = choiceMenu(characterData, startingRoom)
    room = result[1]
    characterData = result[0]
    while 1:
        formatter.clear()
        roomName = room["Name"]
        formatter.drawMenuLine()
        print("Room Name : " + roomName)
        match roomName:
            case "Entry":
                print("You can see a kitchen and a living room from here.")
                print("THere is also a key board with hooks on the wall")
            case "Kitchen":
                print("The Kitchen is mostly bare, with a smattering of cans, pans, and empty boxes.")
                print("The only human touch is a drawing on the fridge.")
            case "Living Room":
                print("A well-worn couch faces an archaic, squat television that carries basic cable only.")
                print("You also see stacks of magazines littered around.")
            case "Hallway":
                print("You are now standing in a hallway, encompassing the rest of the apartment.")
                print("Two sets of doors on each wall stand before you, in a mirror image of each other.")
            case "Bathroom":
                print("This place smells of death. This must have been where Clyde died.")
                print("You feel your sanity slip for a second as you think about him lying in the tub.")
                print("You gag as you think about how gross it must have been for the smell to still linger.")
                print("His death wasn't peaceful. The broken towel rack and cracked shower door tell you this,")
                print("as do the fragments of a broken ceramic toothbrush-holder scattered on the floor.")
                characterData["DerivedStats"]["San"] -= 1
                print("DEBUG: Player Sanity now " + str(characterData["DerivedStats"]["San"]))
            case "Linen Closet":
                print("Just a simple linen closet. Right now, all you see are pillow cases, towels, and wash clothes.")
            case "Main Bedroom":
                print("A bedroom with a queen sized bed. Clyde's room. There are pictures on the dresser, no computer in view.")
            case "Bedroom":
                print("There are a lot of documents in here. It is going to take a long time in here.")
        result = choiceMenu(characterData, room)
        room = result[1]
        characterData = result[0]
        if characterData["Current Scene"] == 99:
            return characterData


def choiceMenu(characterData, room):
        formatter.drawMenuLine()
        print("Choices")
        formatter.drawMenuLine()
        print("1. Move to another room")
        if "Inspect" not in room.keys():
            print("X. Nothing to inspect in this room.")
        else:
            print("2. Inspect this room")
        if "Actions" not in room.keys():
            print("X. No actions in room")
        else:
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
                    room = apartment[roomName]
                case 2:
                    buildingHelper.inspectRoom(room, descriptionDictionary)
                case 3:
                    characterData = buildingHelper.actionsInRoom(room, characterData)
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


def oldLadyBedroom(characterData):
    print("As you are tearing apart the room, you hear a knock at the door. When the knocked stops, you hear a *yip*.")
    checkInput = input("Press 1 to check the door. Press anything else to ignore.\n")
    check = checkInput.isnumeric()
    if check:
        if int(checkInput) == 1:
            print("You look out the door. An old lady with a tiny lap dog waits impatiently outside.")
            print("You open the door with your best smile. 'Hello. How can I help you?'")
            print("'Ohhh, you are so polite. I'm Ms. Clark. I live down below. I heard noises in Clyde's room.'")
            print("'It is just tragic what happened to him. Did you know him?")
            print("'Yes, ma'am. He was my superior. I hope Cassie is doing ok.'")
            input("Press any key to see if she is suspicious of you...\n")
            persuadeCheck = handler.persuadeRoll(characterData)
            if persuadeCheck:
                print("'Oh dear. Poor baby. Have you heard from the family?")
                print("'I hear they are coming into town soon. They have been very private, with the loss and everything.'")
                print("She seems satisfied with this response. 'Well, if you need anything from me, I'm below.'")
                print("She shuffles away to let the demon she is carrying go to the bathroom outside.")
                input("Press any key to close the door...\n")
            else:
                print("She thinks you are being a little too nice. Maybe a little transparent.")
                print("You know exactly what this nosy old lady is going to say before she says it.")
                print("Ummm...I hate to be a worrywart, but can I see your ID?")
                print("You hand it to her")
                input("Press any key to see if she can see through your ID...\n")
                n = handler.roll(100)
                if n <= 80:
                    print("She seems to take forever to eyeball your ID, but she hands it back, seemingly satisfied.")
                    print("'Well, if you need anything, I will be downstair, dearie.' ")
                    print("She seems to give you a side eye as she walks away")
                    print("Hopefully, she doesn't become your next mission...")
                    input("Press any key to close the door...\n")
                else:
                    print("She doesn't seem satisfied with your ID.")
                    print("'I have seen Clyde's badge before...and my memory is good...'")
                    print("'...yours doesn't look like his does...'")
                    print("You give a hardy chuckle. 'That's because Clyde was a dinosaur!'")
                    print("Ms. Clark gives you a disapproving look as she clutches her dog and walks away.")
                    print("Young whippersnappers these days...they have no respect...")
                    input("Press any key to shake your head and close the door...\n")
        else:
            print("DEBUG : Old Lady Ignored.")
    else:
        print("DEBUG : Old Lady Ignored")
    return characterData