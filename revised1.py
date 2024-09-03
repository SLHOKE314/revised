import random
import time

print("Hello! Today you are going to help me tell a story.")
print("First, I am going to ask you some questions and after you type your answer press enter.")
print("Let's begin.")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    # 5 Questions before the story begins
    name = input(f"\nWhat is your name?  ")
    while len(name) == 0:
        name = input(f"Please tell me your name:  ")
        
    childhood_fear = input(f"\nWhat were you scared of most as a kid? ")
    while len(childhood_fear) == 0:
        childhood_fear = input(f"Please tell me your childhood fear:  ")
        
    
        
    atefor_lunch = input(f"\nWhat did you eat for lunch today?  ")
    while len(atefor_lunch) == 0:
        atefor_lunch = input(f"Please tell me what you had for lunch today.  ")
        
    horror_film = input(f"\nAs a kid, what movie scared you the most?  ")
    while len(horror_film) == 0:
        horror_film = input(f"Please tell me a movie that scared you:  ")

    # Inventory initialization
    inventory = []
        
    # Story begins
    print(f"\n{name}, {name}....It's getting louder and louder...{name}....")
    print(f"You find yourself walking the streets in the small neighborhood you grew up in.")
    print(f"\nYou're wandering around confused and something is pulling you to the {scary_place}.")
    print(f"\nYou look up the long drive and there it is....{scary_place}.")
    print(f"\nFlashbacks come flooding back to you sending a chill down your spine. You cringe at the thought of {childhood_fear}.")
    print(f"\nYour hand involuntarily moves and opens the gate. You don't want to go in but something is pulling you and you can't turn around.")
    print(f"\nThis place reminds you of {horror_film}. But in all reality, it has dark secrets of its own.")

    # Decision point: Do you go through the gate?
    theCalling = input(f"\nDo you enter the gate and find what is pulling you back here after all these years? Please type yes or no:  ")
    while theCalling.lower() != "yes" and theCalling.lower() != "no":
        theCalling = input("Please type yes or no:  ")
    
    if theCalling.lower() == "yes":
        print(f"\nYou give in to whatever is pulling you and push the gate open. It creaks like nails on a chalkboard.")
        print(f"The sound startles some black birds nearby and they squawk as they fly off. You think to yourself, could this get any more creepy? ")
        print(f"You are walking up the drive and as you're nearing the main entrance, panic sets in. You take deep breaths and tell yourself it's time to face your fears. Nothing can hurt you. ")
        print(f"You push the main door open and are slightly surprised at how heavy the door is. You walk inside and the door slams shut. Couldn't have been the wind pushing that heavy door too.")
        print(f"\nThe smell of rotten {atefor_lunch} slaps you in the face. You almost vomit at the stench.")
        print(f"You tell yourself it's time to face your fears. You have always been scared of {horror_film}.")
        print(f"You see something shining in the moonlight. You walk over towards it and what do you know.")
        print(f"It's a key!")
        
        # Add key to inventory
        inventory.append("key")
        print(f"You pick up the key and put it in your inventory: {inventory}")

        # Decision 1: Explore the house or leave
        explore = input(f"\nDo you want to explore the house or leave? Type explore or leave:  ")
        while explore.lower() != "explore" and explore.lower() != "leave":
            explore = input("Please type explore or leave:  ")

        if explore.lower() == "explore":
            print(f"\nYou venture deeper into the house, feeling every creak of the floor beneath your feet.")
            time.sleep(2)
            print(f"There are two doors in front of you: one to the left and one to the right. Which do  you choose?")

            door_choice = input("Type left or right:  ")
            while door_choice.lower() != "left" and door_choice.lower() != "right":
                door_choice = input("Please type left or right:  ")


            if door_choice.lower() == "left":
                print(f"\nYou open the left door and find an old, dusty library filled with books. Suddenly, a ghostly apparition appears!")
                action = input("Do you want to (1) confront the ghost or (2) throw the key at it? Type 1 or 2: ")
                if action == "1":
                    print(f"You try to confront the ghost but it starts violently wailing and flies straight towards you. The ghost posses you and you are never seen or heard from again.")

                elif action == "2":
                    print(f"You throw the key at the ghost, and it laughs. The key passes through it and clatters to the ground. Suddenly, all the doors start slamming. ")
                    print(f"You manage to run through one of the doors and escape safefully.")

            else:
                print(f"\nYou open the right door and find a creepy cellar. As you step down the door slams shut behind you.")
                print(f"You are trapped forever. No one will ever hear you scream for help.")  
        
    # Decision 2
    whatto_do = input(f"\nYou've been in a stare down with this thing for about 5 minutes now. Do you run? (yes or no):  ")
    while whatto_do.lower() != "yes" and whatto_do.lower() != "no":
        whatto_do = input("Please type yes or no:  ")

    if whatto_do.lower() == "yes":
        print(f"\nYou start to turn and run away, but the thing grabs the back of your shirt and pulls you down.")
        print(f"You land on your back. The thing leans over you and gives you a creepy smirk.")

    # Alternate Endings
    if theCalling.lower() == "yes" and whatto_do.lower() == "yes":
        print(f"\nThe thing drags you down to the basement. You are never seen or heard from again. You become part of the legend. You spend eternity in {scary_place}.")
    elif theCalling.lower() == "no" and whatto_do.lower() == "no":
        print(f"\nConfused, the dark figure slowly backs away wondering why you didn't try to run. It dashes away through the woods and you manage to escape.")
    else:
        print(f"You manage to break free from the trap and scramble to your feet.")
        print(f"You trip and fall down.")
        print(f"The thing grabs you by the hair and drags you away. Never to be seen again.")

    # Ask to play again
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no: ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")
