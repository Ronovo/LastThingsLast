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
input("Press any key to continue...\n")
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
    try:
        menuNumber = int(menuInput)
        formatter.clear()
        match menuNumber:
            case 1:
                newCharacterData = CharacterHelper.createNewCharacter()
                Game.game.startGame(newCharacterData)
            case 2:
                loadedCharacter = CharacterHelper.getCharacterMenu()
                Game.game.startGame(loadedCharacter)
            case 3:
                loadedCharacter = CharacterHelper.getCharacterMenu()
                CharacterHelper.checkCharacterMenu(loadedCharacter)
            case 4:
                quit()
    except TypeError:
        input("Invalid Input. Press anything to try again...")