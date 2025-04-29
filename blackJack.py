import random
#imported random so the cards can be shuffled
import time
#this makes it feel more like a game cuz the cards need time to shuffle

def blackjack():
    #made a function called blackjack and then made card variables so we can play
    
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    cards = ["2", "3", "4", "5", "6", "7", "8","9","Jack", "Queen", "King","Ace"]
    #these are all are cards and suits. now we gotta get all possible outcomes.
    
    deck = [(suit,card) for suit in suits for card in cards]
    #now we have a full deck.
    
    #we need to shuffle and give out some cards so this is the shuffle.
    giveOutCards = 2
    givenCards = random.sample(deck,giveOutCards)
    
    #this is are middle man so we can pass this to the player by printing it.
    cardOne_cards , cardOne_suits = givenCards[0]
    cardTwo_cards , cardTwo_suits = givenCards[1]
   
    
    #this concenates them together , for example "ace of spades"
    card1 = f"{cardOne_suits} of {cardOne_cards}"
    card2 = f"{cardTwo_suits} of {cardTwo_cards}"
   
    
    #welcome and rules
    print("  \n\n")
    print("Welcome to the BlackJack Table!")
    print("___________________________________________\n\n\n")
    print("The rules are simple:\n")
    print("(__First to 21 wins__)\n")
    print("(__First round is on the house__)\n")
    print("(__First to bust pays for drinks 😁__)\n\n")
    
    #ask player if they want to play
    player = input("would you like to play a round of 21:\n________________________________________\n\n\n\n\n\n")
    if player.lower() == "yes": 
        print("  \n\n")        
        print("Take a seat while i shuffle some cards\n\n")
        time.sleep(3)
        print(f"here is your cards:\n\n\nThe {card1} and The {card2}\n\n")
        #the conditionals here are just fun banter, i plan on adding much more and making it random o it doesnt get old. 
        #also i wanna give the player some money for listening to the banter.
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
        else:
            print("good luck kid\n\n ")      
               
               
    #if player doesnt want to play.
    else:
        print("GTFO of here dumb@$$ leave room for the real ballers")
blackjack()
    
    

    
        
            