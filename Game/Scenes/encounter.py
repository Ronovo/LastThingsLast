from logging import DEBUG

import formatter
from Game.Logic.actions import roll


def startEncounter(characterData):
    formatter.clear()
    print("You freeze at the sound. What the fuck? Is someone in the septic tank?")
    print("Why? How? As you sit there, thinking through the situation, you hear the voice again.")
    print("'I know you are there....I heard you....please, I'm desperate'")
    print("The note told you not to look in. What do you want to do?")
    while 1:
        print("1. Open and look inside")
        print("2. Get the gas from the shed and start pouring.")
        openInput = input("Please make your choice...\n")
        if openInput.isnumeric():
            formatter.clear()
            num = int(openInput)
            match num:
                case 1:
                    characterData["Investigation Log"]["Septic Tank"].append("Looked in the tank.")
                    characterData["Investigation Log"]["Septic Tank"].append("Saw Marlene Zombie")
                    print("You open the tank and look inside. You can't believe your eyes.")
                    damage = roll(4)
                    characterData["DerivedStats"]["San"] -= damage
                    print("You feel your sanity slip by " + str(damage))
                    print("DEBUG: Sanity now at " + str(characterData["DerivedStats"]["San"]))
                    print("A corpse, wasted and rotten from so many years in the dank hole.")
                    print("She turns from the sun, and scatters for the dark, like a roach.")
                    print("From the shadow, a frail voice calls to you. 'the light...so long....the light...'")
                    print("You ask her to come out into the light, and you get a good look at her: Skin sloughing off her face;")
                    print("What little hairs left on her head stringy and wet and clinging to her blue-grey skin;")
                    print("Strange marking carved all over her body, long emptied of any blood.")
                    print("You don't need any other knowledge then that.")
                    input("Press enter to lock the tank and get the gas...\n")

                    print("You start to gather the gas as she starts to talk to you in your mind.")
                    print("Why did you close the lid on me? Does my appearence scare you?")
                    print("You stop, as hearing her voice in your head sinks in.")
                    print("You shake you head, and gather the supplies...")
                    input("Press enter to start pouring...\n")

                    print("As you pour, the voice begins to talk more insistently in your head.")
                    print("At first, begging. Then bargaining. Telling you she can tell you secrets of the afterlife.")
                    print("She can tell you the lottery numbers of any state of any year within a range of 100 years.")
                    print("Her voice starts to falter and lose the old lady sheen as it offers to knowledge of an eldritch nature")
                    print("Your brain fills with words you can't understand as you focus on pouring.")
                    damage = roll(4)
                    characterData["DerivedStats"]["San"] -= damage
                    print("You feel your sanity slip by " + str(damage))
                    input("Press enter to light the gas...\n")

                    print("You hear her shout and splash towards the opening as you drop the lighter in.")
                    print("Slamming the hatch shut, you are just in time as she bangs against it.")
                    print("She screams as the gas fire engulfs her, and she stops banging against the hatch at some point.")
                    input("Press enter to walk away...\n")

                    break
                case 2:
                    characterData["Investigation Log"]["Septic Tank"].append("Decided to burn the thing in the tank.")
                    print("You decide to heed the note's advice. You start to head to the shed to grab the cans.")
                    print("You carry over the cans to the opposite side of the septic tank from the voice.")
                    print("These little locks are easy enough to pick when you know what you are doing.")
                    print("As you fumble with it, you hear splashing below you.")
                    print("Not looking in, you start to blindly pour gas in.")
                    input("Press enter to continue...\n")

                    print("'No please...what are you doing!!?? Is that gas? Are you going to kill me?!'")
                    print("The presumably woman's voice gets louder, and you hear scratching from inside,")
                    print("As if she is clawing at the walls, as she wails. 'nooooOOOOO!!!!!'")
                    input("Press enter to brace the lid...\n")

                    print("Your long years of being an interrogator mean you have seen a lot of people who were very helpless.")
                    print("They never acted like whoever...or whatever...is in this tank.")
                    print("In a last ditch effort, you hear her say 'Please....it's Marlene...please don't do this!'")
                    input("Press enter to continue pouring the next can...\n")

                    print("'Please, Clyde did some kind of....dark magic? I don't know...all I know is I'm cold...and I'm scared.'")
                    print("You silently pour. Not engaging with 'Marlene'. Dark magic would explain how she is alive down there.")
                    print("You already know from your reports, she is dead. Whatever is down there, it can't be Marlene.")
                    print("There is still a human part of you that feels a tug as you hear her pleading.")
                    print("You have killed people before. Hell, you might have killed one or two things that weren't of this world.")
                    input("Press enter to resist, and do your job...")

                    characterData["DerivedStats"]["WP"] -= 3
                    print("DEBUG : Willpower now at " + str(characterData["DerivedStats"]["WP"]))
                    print("You click the zippo lighter you found in the shed, next to the cans.")
                    print("'Goodbye, Marlene'. You walk away as the lighter drops down. The shrieks will haunt your dreams forever.")
                    characterData["DerivedStats"]["San"] = 69
                    print("DEBUG : Sanity at 69")
                    break
                case _:
                    print("Invalid option. Please try again.")
                    input("Press enter to continue...\n")
        else:
            print("Invalid option. Please try again.")
            input("Press enter to continue...\n")
    formatter.clear()
    print("Starting at a wailing pitch, converting into sounds that no human throat can emit, the screams never stop.")
    print("Though the sounds will echo through your mind for eons, you feel a relief that the job is over.")
    input("Press enter to finish the mission...\n")
    print("\n")
    characterData["Current Scene"] = 0
    return characterData