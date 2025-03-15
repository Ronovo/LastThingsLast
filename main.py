import CharacterHelper
import Game.game
import formatter


formatter.clear()
formatter.drawMenuLine()
print("Welcome to Last Things Last V0.1")
print("Ronovo's First Full Delta Green Scenario")
formatter.drawMenuLine()
print("Welcome to your first assignment for the shadowy side of the government!")
print("You will take on the role of an FBI agent tasked with cleaning up after a dead IRS officer.")
print("What starts as a routine sweep will lead down a path where there is no return.")
input("Press enter to continue...\n")
while 1:
    formatter.clear()
    formatter.drawMenuLine()
    print("Main Menu")
    formatter.drawMenuLine()
    print("1. New Game")
    print("2. Load Game")
    print("3. Check Character Sheet")
    print("4. Quit")
    menuInput = input("Please select your answer...\n")
    if menuInput.isnumeric():
        menuNumber = int(menuInput)
        formatter.clear()
        match menuNumber:
            case 1:
                newCharacterData = CharacterHelper.createNewCharacter()
                Game.game.startGame(newCharacterData)
            case 2:
                loadedCharacter = CharacterHelper.getCharacterMenu()
                if loadedCharacter is not None:
                    Game.game.startGame(loadedCharacter)
            case 3:
                loadedCharacter = CharacterHelper.getCharacterMenu()
                if loadedCharacter is not None:
                    CharacterHelper.checkCharacterMenu(loadedCharacter)
            case 4:
                quit()
            case _:
                input("Invalid Input. Press anything to try again...")
    else:
        input("Invalid Input. Press anything to try again...")