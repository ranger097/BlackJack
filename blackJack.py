import random
import time

def blackJack():
    
    #this section gives us our card deck with included suits and numbers
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    cards = ["2", "3", "4", "5", "6", "7", "8","9","Jack", "Queen", "King","Ace"]
    
    #this section instead of shuffling the deck, assigns a random 5 cards every game
    deck = [(suit,card) for suit in suits for card in cards]
    giveOutCards = 10
    givenCards = random.sample(deck,giveOutCards)
    
   #this section takes a random suit and ties it to a random card, there are 10 cards
    cardOne_cards , cardOne_suits = givenCards[0]
    cardTwo_cards , cardTwo_suits = givenCards[1]
    cardThree_cards , cardThree_suits = givenCards[2]
    cardFour_cards , cardFour_suits = givenCards[3]
    cardFive_cards , cardFive_suits = givenCards[4]
    cardSix_cards , cardSix_suits = givenCards[5]
    cardSeven_cards , cardSeven_suits = givenCards[6]
    cardEight_cards , cardEight_suits = givenCards[7]
    cardNine_cards , cardNine_suits = givenCards[8]
    cardTen_cards , cardTen_suits = givenCards[9]
    
    #this is are values section where we will add the cards.
    valueOne = cardOne_suits
    valueTwo = cardTwo_suits
    totalValue = valueOne + valueTwo
    firstHitValue = totalValue + cardThree_suits
    secondHitValue = firstHitValue + cardFour_suits
    thirdHitValue = secondHitValue + cardFive_suits
    forthHitValue = thirdHitValue + cardSix_suits
    fifthHitValue = forthHitValue + cardSeven_suits
    sixthHitValue = fifthHitValue + cardEight_suits
    seventhHitValue = sixthHitValue + cardNine_suits
    eighthHitValue = seventhHitValue + cardTen_suits
    
    
    #this section formats are code ex: king of spades
    card1 = f"{cardOne_suits} of {cardOne_cards}"
    card2 = f"{cardTwo_suits} of {cardTwo_cards}"
    card3 = f"{cardThree_suits} of {cardThree_cards}"
    card4 = f"{cardFour_suits} of {cardFour_cards}"
    card5 = f"{cardFive_suits} of {cardFive_cards}"
    card6 = f"{cardSix_suits} of {cardSix_cards}"
    card7 = f"{cardSeven_suits} of {cardSeven_cards}"
    card8 = f"{cardEight_suits} of {cardEight_cards}"
    card9 = f"{cardNine_suits} of {cardNine_cards}"
    card10 = f"{cardTen_suits} of {cardTen_cards}"
    
    #this section is the welcome screen, explaining the rules
    print("  \n\n")
    print("Welcome to the BlackJack Table!")
    print("___________________________________________\n\n\n")
    print("The rules are simple:\n")
    print("(__First to 21 wins__)\n")
    print("(__First round is on the house__)\n")
    print("(__First to bust pays for drinks 😁__)\n\n")
    
    #this section ask the player if they would like to play
    decide = ["> 1. Yes\n\n", "> 2. No\n\n"]
    print("would you like to play a round of 21:\n________________________________________\n\n")
    
    #this loop is for options, like yes or no
    for i in range(2):
        print(decide[i])
        i = i + 1
        
    #this gets player input
    x = input("")
    if x == "1": 
        print("  \n\n")        
        print("Take a seat while i shuffle some cards\n\n")
        time.sleep(3)
        print(f"here is your cards:\n\n\nThe {card1} and The {card2}\n\n")
        
        #this is for dealer banter if the suits are the same
        
        #hearts
        if cardOne_cards == "Hearts" and cardTwo_cards == "Hearts":
            print("Hearts huh?\n\n")
            print("Dont fall in love kid\nbiggest mistake i ever made")
            
        #clubs
        elif cardOne_cards == "Clubs" and cardTwo_cards == "Clubs":
            print("See those clubs?\n\n")
            print("They're like the nights here.\nDark, a little rough around the edges,\nand you never know what's gonna hit ya.\nJust try not to get hit too hard, eh?")
            
        #diamonds
        elif cardOne_cards == "Diamonds" and cardTwo_cards == "Diamonds":
            print("See those diamond?\n\n")
            print("Pretty.\nProbably Worth something.\nBut you gotta know when to hold 'em, kid.\nAnd more importantly,\nwhen to walk away from 'em.\nLearned that the hard way...\na few times.")
            time.sleep(1)
            print("give me a second kid\n")
            time.sleep(2)
            print("alright lets play\n")
            
        #spades
        elif cardOne_cards == "Spades" and cardTwo_cards == "Spades":
            print("spades damn?\n\n")
            print("you wouldnt happen to\nknow any spades do you?\nsome guy named David\ncame in here acting like a total idiot\nat first it was funny\nbut he ran off with the coins\n\nand never tipped the bartenders either")
            
        #this is to get player input if they would like the ace to be a 1 or 11    
        elif cardOne_cards == "Ace" or cardTwo_cards == "Ace":
            x = input("Ace? cool....\n1 or 11?\n")
            if x == "11":
                "Ace" == "11"
        else:
            "Ace" == "1"
            print("good luck kid\n\n ")      
    else:
        print("GTFO of here dumb@$$ leave room for the real ballers")
        
    #starting player decisions and dealer banter
    options = ["> 1. thanks\n", 
               "> 2. youll need the luck\n", 
               "> 3. just play the fucking game old man\n"]
    
    #this loops through the availble options and prints them to the console
    for i in range(3):
        print(options[i])
        i = i + 1
    
    #this gets player input for decisoions
    x = input("choose:\n\n")
    if x == "1":
        print("you got it\n\n\n")
    elif x == "2":
        print("you got guts kid\n\n\n")
    else:
        print("lifes a game kid, dont rush it\n\n\n")
        
    #this will let the player know the total value
    #then it ask them if they would like to take a hit
    print(f"Hit? your at {totalValue}")
    choose = ["> 1. Sure", "> 2. Nah"]
    for i in range(2):
        print(choose[i])
        i = i + 1
    
    x = input("choose: \n\n")
    if x == "1":
        print("Here: \n")
        print(f"{card3}\n")
        print(f"alright your at {card1}, {card2}, and {card3}\n\n")
        if totalValue > 21:
            print("you went bust kid\n\n")
            print("again\n\n")
            options = ["> 1. Yes\n\n", 
                       "> 2. No\n\n"]
            for i in range(2):
                print(options[i])
                i = i + 1
            x = input("")
            if x == "1":
                blackJack()
            else:
                print("see you again kid")
    else:
        print("smart\n\n")
        print(f"so your at {card1} and {card2}\n\n")
        print(f"while im at {card3} and {card4}")
        
       
       
       
       
       
       
blackJack()
    
    

    
        
            