import formatter


def objectives(characterData):
    while 1:
        formatter.clear()
        formatter.drawMenuLine()
        print("Objectives Menu")
        formatter.drawMenuLine()
        print("1. Mission Objectives")
        print("2. Baughman Information")
        print("3. Items to be received")
        print("4. Continue with your mission...")
        menuInput = input("Please select your answer...\n")
        check = menuInput.isnumeric()
        if check:
            menuNumber = int(menuInput)
            formatter.clear()
            match menuNumber:
                case 1:
                    print("-Proceed to residence of Clyde Baughman.")
                    print("-Remove any evidence of The Program's activities")
                    print("-Baughman's heirs are expected within 48 hours. Make sure everything is clean by then.")
                    print("-Involve no one else in this operation")
                    print("-Meet back in this room in 48 hours.")
                    print("-If you find signs that Baughman violated Delta Green security, report them.")
                case 2:
                    print("Clyde Baughman, Died at 64 from heart attack.")
                    formatter.drawMenuLine()
                    print("Family :")
                    print("-Wife: Marlene (8/20/1948 - 11/2/2002")
                    print("-Daughter : Sharon (9/12/1967 - Present)")
                    print("-Son : Michael (7/28/1974 - Present)")
                    formatter.drawMenuLine()
                    print("Employer(Former) : Bureau of Internal Revenue(Later IRS)")
                    print("Active from: 6/11/1965-9/1/1999")
                    print("Status : Retired")
                    print("Title: Assistant Deputy Commissioner for Operational Support")
                    formatter.drawMenuLine()
                    print("Program Affiliation")
                    print("-Active : 1967 - 1970")
                    print("-Numerous consultations with a specialty in taxation and property confiscation.")
                    print("-No current association with The Program.")
                    formatter.drawMenuLine()
                case 3:
                    print("For this mission, you will be given:")
                    print("-An IRS Agent Badge. No official, but will hold up if not scrutinized")
                    print("-Burner Phone with one number programmed in it: Hands.")
                    print("-Car keys and a rental car, parked outside.")
                case 4:
                    return characterData
                case _:
                    print("Invalid option! Please try again.")
            input("Press enter to continue...\n")



def briefing(characterData):
    formatter.clear()
    formatter.drawMenuLine()
    print("SCENE 1")
    formatter.drawMenuLine()
    print("Iowa City, Iowa")
    print("It is currently Thursday, May 10th, 2010. You are in a room getting the briefing on your assignment.")
    print("We will learn more about how you got here later.")
    print("A man walks into the room, and stands across from you. 'Thank you for showing up on short notice.'")
    print("'Most task force meetings we have are very high priorty, and short notice, so you better get used to it.'")
    print("'I am Agent Hands. You can call me that, or Mr. Hands. And you are?'")
    input("Press enter to say your name...\n")

    print("'I'm " + characterData['Agent Name'] + "' you respond. You assume he already knows your real name.")
    print("After all, you are off work today because someone submitted time off requests in your name.")
    print("Time off you were not aware of...")
    print("'It's nice to meet you, " + characterData['Agent Name'] + ". Let's get down to business...'")
    input("Press enter to get your assignment...\n")

    print("'You are here to do some clean-up on a former Associate. Clyde Baughman. Died of natural causes. As far as we know.")
    print("We are not concerned with how he died. All we are concerned about is any information that leads back to us.")
    print("He was active years ago, and when he was decommissioned from the Program, We did an initial security check.")
    print("Nothing was found then, but it never hurts do trust, but verify, right?'")
    print("He hands you a paper handout with information on it")
    input("Press enter to get more information...")

    formatter.clear()
    objectives(characterData)
    print("You step outside into the bright sun. As the door closes behind you,")
    print("you look back and shake your head. Meeting a 'Man in Black' in a Post Office")
    print("in Iowa City was not on the list of things you planned on doing with your weekend.")
    print("But, you have a job to do. You press the unlock button on the key fob.")
    print("The lights blink, the horn honks, and your chariot, a 2008 Black Toyota Camry, awaits.")
    input("Press enter to get in the car and drive...")

    #Scene Change Logic Here
    characterData["Current Scene"] = 99
    characterData["Next Scene"] = 2
    characterData["Armor/Gear"].append("Burner Phone")
    characterData["Armor/Gear"].append("IRS Badge")
    characterData["Armor/Gear"].append("Car Keys")
    characterData["Armor/Gear"].append("Apartment Key")
    return characterData