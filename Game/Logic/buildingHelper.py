import formatter
from Game.Logic import actions


def moveRoom(room):
    n = 1
    index = 0
    numberOfRooms = len(room["Rooms"])
    if numberOfRooms > 1:
        for x in room["Rooms"]:
            print(str(n) + ". " + x)
            n += 1
        roomInput = input("Please select the next room...\n")
        check = roomInput.isnumeric()
        if check:
            index = int(roomInput) - 1

    print("Moving to " + room["Rooms"][index])
    input("Press enter to move...\n")
    return room["Rooms"][index]

def inspectRoom(characterData,room,descriptionDictionary):
    while 1:
        formatter.clear()
        n = 1
        if "Inspect" not in room.keys():
            print("There is nothing to inspect in this room.")
            input("Press anything to return to the Choices menu")
            return
        else:
            for x in room["Inspect"]:
                print(str(n) + ". " + x)
                n += 1
            print(str(n) + ". Return to Choices Menu")
            inspectInput = input("Please select the thing you want to inspect...\n")
            check = inspectInput.isnumeric()
            if check:
                if int(inspectInput) == n:
                    return characterData
                else:
                    index = int(inspectInput) - 1
                    objectName = room["Inspect"][index]
                    formatter.drawMenuLine()
                    print(descriptionDictionary[objectName])
                    if objectName == "Bed":
                        room["Inspect"].append("Note")
                    if objectName == "Note":
                        characterData["Investigation Log"]["Cabin"].append("Read Clyde's Note.")
                    input("Press enter to continue...\n")
            else:
                input("Invalid Input. Press anything to try again...")



def actionsInRoom(room, characterData, nextScene):
    while 1:
        formatter.clear()
        n = 1
        if "Actions" not in room.keys():
            print("There are no actions in this context.")
            input("Press anything to return to the Choices menu")
            return characterData
        else:
            for x in room["Actions"]:
                print(str(n) + ". " + x)
                n += 1
            print(str(n) + ". Return to Choices Menu")
            actionInput = input("Please select the thing you want to inspect...\n")
            check = actionInput.isnumeric()
            if check:
                if int(actionInput) == n:
                    return characterData
                else:
                    index = int(actionInput) - 1
                    objectName = room["Actions"][index]
                    formatter.drawMenuLine()
                    actions.serveAction(objectName, characterData)
                    input("Press enter to continue...\n")
            else:
                input("Invalid Input. Press anything to try again...")
        if "Actions" not in room.keys():
            return characterData
        if characterData["Next Scene"] == nextScene:
            return characterData
