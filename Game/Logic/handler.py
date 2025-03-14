from Game.Logic.actions import roll

## GENERAL ROLLS
def luckRoll():
    luckCheck = roll(100)
    if luckCheck < 51:
        return True
    else:
        return False

def persuadeRoll(characterData):
    check = roll(100)
    print("DEBUG : Persuade roll : " + str(check))
    if check < characterData["Skills"]["Persuade"]:
        return True
    else:
        return False
