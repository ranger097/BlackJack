import random
#imported random so the cards can be shuffled
import time
#this makes it feel more like a game cuz the cards need time to shuffle

def blackjack():
    #made a function called blackjack and then made card variables so we can play
    
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    cards = ["2", "3", "4", "5", "6", "7", "8","9","jack", "queen", "king","ace"]
    #these are all are cards and suits. now we gotta get all possible outcomes.
    
    deck = [(suit,card) for suit in suits for card in cards]
    #now we have a full deck.
    
    #we need to shuffle and give out some cards so this is the shuffle.
    giveOutCards = 5
    givenCards = random.sample(deck,giveOutCards)
    
    #this is are middle man so we can pass this to the player by printing it.
    cardOne_cards , cardOne_suits = givenCards[0]
    cardTwo_cards , cardTwo_suits = givenCards[1]
    cardThree_cards, cardThree_suits = givenCards[2]
    cardFour_cards, cardFour_suits = givenCards[3]
    cardFive_cards, cardFive_suits = givenCards[4]
    
    #this concenates them together , for example "ace of spades"
    card1 = f"{cardOne_suits} of {cardOne_cards}"
    card2 = f"{cardTwo_suits} of {cardTwo_cards}"
    card3 = f"{cardThree_suits} of {cardThree_cards}"
    card4 = f"{cardFour_suits} of {cardFour_cards}"
    card5 = f"{cardFive_suits} of {cardFive_cards}"
    
    #welcome and rules
    print("  \n\n")
    print("Welcome to the BlackJack Table!")
    print("___________________________________________\n\n\n")
    print("The rules are simple:\n")
    print("#First to 21 wins\n")
    print("#First round is on the house\n")
    print("#First to bust pays for drinks 😁.\n\n")
    
    #ask player if they want to play
    player = input("would you like to play a round of 21:\n________________________________________\n\n\n\n\n\n")
    if player == "yes": 
        print("Take a seat while i shuffle some cards\n\n")
        time.sleep(3)
    else:
        print("GTFO of here dumb@$$ leave room for the real ballers")
        print(f"here is your cards:\n The {card1} and The {card2}\n\n")
        
        
        if cardOne_suits and cardTwo_suits == "Hearts":
            print("Hearts huh?\n\n")
            print("Dont fall in love kid\nbiggest mistake i ever made")
        if cardOne_suits and cardTwo_suits == "Clubs":
            print("See those clubs?\n\n")
            print("They're like the nights here.\nDark, a little rough around the edges,\nand you never know what's gonna hit ya.\nJust try not to get hit too hard, eh?")
        if cardOne_suits and cardTwo_suits == "Diamonds":
            print("See those diamond?\n\n")
            print("Pretty.\nProbably Worth something.\nBut you gotta know when to hold 'em, kid.\nAnd more importantly,\nwhen to walk away from 'em.\nLearned that the hard way...\na few times.")
            print("give me a second kid\n")
            time.sleep(2)
            print("alright lets play\n")
            
        if cardOne_suits and cardTwo_suits == "Spades":
            print("spades damn?\n\n")
            print("you wouldnt happen to\nknow an spades do you?\nsome guy named David\ncame in here acting like a total idiot\nat first it was funny\nbut he ran off with the coins\n\nand never tipped the bartenders either")
    


blackjack()
    
    

    
        
            