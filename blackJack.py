import random
import time

def blackJack():
    
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    cards = ["2", "3", "4", "5", "6", "7", "8","9","Jack", "Queen", "King","Ace"]
    deck = [(suit,card) for suit in suits for card in cards]
    giveOutCards = 5
    givenCards = random.sample(deck,giveOutCards)
    
    
    cardOne_cards , cardOne_suits = givenCards[0]
    cardTwo_cards , cardTwo_suits = givenCards[1]
    cardThree_cards , cardThree_suits = givenCards[2]
    cardFour_cards , cardFour_suits = givenCards[3]
    cardFive_cards , cardFive_suits = givenCards[4]
    
    
    card1 = f"{cardOne_suits} of {cardOne_cards}"
    card2 = f"{cardTwo_suits} of {cardTwo_cards}"
    card3 = f"{cardThree_suits} of {cardThree_cards}"
    card4 = f"{cardFour_suits} of {cardFour_cards}"
    card5 = f"{cardFive_suits} of {cardFive_cards}"
    
    print("  \n\n")
    print("Welcome to the BlackJack Table!")
    print("___________________________________________\n\n\n")
    print("The rules are simple:\n")
    print("(__First to 21 wins__)\n")
    print("(__First round is on the house__)\n")
    print("(__First to bust pays for drinks 😁__)\n\n")
    
    player = input("would you like to play a round of 21:\n________________________________________\n\n\n\n\n\n")
    if player.lower() == "yes": 
        print("  \n\n")        
        print("Take a seat while i shuffle some cards\n\n")
        time.sleep(3)
        print(f"here is your cards:\n\n\nThe {card1} and The {card2}\n\n")
        if cardOne_suits == "Hearts" and cardTwo_suits == "Hearts":
            print("Hearts huh?\n\n")
            print("Dont fall in love kid\nbiggest mistake i ever made")
        elif cardOne_suits == "Clubs" and cardTwo_suits == "Clubs":
            print("See those clubs?\n\n")
            print("They're like the nights here.\nDark, a little rough around the edges,\nand you never know what's gonna hit ya.\nJust try not to get hit too hard, eh?")
        elif cardOne_suits == "Diamonds" and cardTwo_suits == "Diamonds":
            print("See those diamond?\n\n")
            print("Pretty.\nProbably Worth something.\nBut you gotta know when to hold 'em, kid.\nAnd more importantly,\nwhen to walk away from 'em.\nLearned that the hard way...\na few times.")
            time.sleep(1)
            print("give me a second kid\n")
            time.sleep(2)
            print("alright lets play\n")
        elif cardOne_suits == "Spades" and cardTwo_suits == "Spades":
            print("spades damn?\n\n")
            print("you wouldnt happen to\nknow any spades do you?\nsome guy named David\ncame in here acting like a total idiot\nat first it was funny\nbut he ran off with the coins\n\nand never tipped the bartenders either")
        elif cardOne_cards == "Ace" or cardTwo_cards == "Ace":
            x = input("Ace? cool....\n1 or 11?\n")
            if x == "11":
                "Ace" == "11"
        else:
            "Ace" == "1"
            print("good luck kid\n\n ")      
    else:
        print("GTFO of here dumb@$$ leave room for the real ballers")
        
    
    options = ["> 1. thanks\n", "> 2. youll need the luck\n", "> 3. just play the fucking game old man\n"]
    for i in range(3):
        print(options[i])
        i = i + 1
    x = input("choose:\n\n")
    if x == "1":
        print("you got it\n\n\n")
    elif x == "2":
        print("you got guts kid\n\n\n")
    else:
        print("lifes a game kid, dont rush it\n\n\n")
        
        
    print("Hit?")
    choose = ["> 1. Sure", "> 2. Nah"]
    for i in range(2):
        print(choose[i])
        i = i + 1
    
    x = input("choose: \n\n")
    if x == "1":
        print("Here: \n")
        print(f"{card3}\n")
        print(f"alright your at {card1}, {card2}, and {card3}\n\n")
    else:
        print("smart\n\n")
        print(f"so your at {card1} and {card2}")
       
       
       
       
       
       
blackJack()
    
    

    
        
            