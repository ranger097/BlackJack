#list of libraries for the project
#these are what is needed now
import random
import curses
import time
from curses import wrapper
from curses import window

#these will be needed later
import signal
import sys
import os
import blessed
import readchar

#these are gonna be the frame of the game
#these will be added later
import rich
from rich.live import Live
from rich.table import Table

#makes game screen
stdscr = curses.initscr()

#disables mouse cursor
curses.curs_set(0)
curses.mousemask(0)

#functions to display text in screen corners
def topRight(stdscr, text):
    height, width = stdscr.getmaxyx()
    #cutting the text at the end so it doesnt wrap the terminal
    if len(text) > width:
        #this specificallly cuts it to 1 line
        text = text[:width] 
    #this minuses the width by the length of the text so we get the full wdth minus the text length
    x = width - len(text) 

def bottomRight(stdscr, text):
    height, width = stdscr.getmaxyx()
    if len(text) > width:
        #this specificallly cuts it to 1 line
        text = text[:width] 
    #this minuses the width by the length of the text so we get the full wdth minus the text length
    x = width - len(text)
    y = height - 1
    
def bottomLeft(stdscr, text):
    height, width = stdscr.getmaxyx()
    if len(text) > width:
        text = text[:width]
    y = height - 1
    
def topLeft(stdscr,text):
    height, width = stdscr.getmaxyx()
    if len(text) > width:
        text = text[:width]
    y = height - height + 1
    x = width - width + 1
    
#this function will center arrays of text.
#very useful when writing tons of scripts that need to be called.
def centerText(stdscr,strings):
    height , width = stdscr.getmaxyx()
    num_strings = len(strings)
    
    starting_y = (height - num_strings) // 2
    
    #loop to print our text out
    for i, text in enumerate(strings):
        x =  (width - len(text)) // 2
        y = starting_y + 1
        if len(text) > width:
            text = text[:width]
        
        stdscr.addstr( y , x , text )
             
    stdscr.refresh()





#main game funtion
def blackJack(stdscr):
    legendStatus = 0
    legend = 0
    
    while legendStatus < 100:
        
        stdscr.clear()
        yo, xo = stdscr.getmaxyx()
        y = round(yo/2)
        x = round(xo/2)
        
        #this section gives us our card deck with included suits and numbers
        suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
        Jack = 10
        Queen = 10
        King = 10
        Ace = 1
        
        cards = [ 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , Jack, Queen, King , Ace ]
    
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
        stdscr.addstr(y - 4, x ,"Welcome to the BlackJack Table!")
        stdscr.addstr(y - 2, x ,"The rules are simple:")
        stdscr.addstr(y + 0, x ,"(__First to 21 wins__)")
        stdscr.addstr(y + 2, x ,"(__First round is on the house__)")
        stdscr.addstr(y + 4, x ,"(__First to bust pays for drinks 😁__)")
        stdscr.addstr(y + 6 , x ,"Press 1 to continue")
        
        #this gets player input
        player_input = stdscr.getch()
        if player_input == ord('1'): 
            stdscr.clear()
            stdscr.refresh()       
            stdscr.addstr(y - 2 , x ,"Take a seat while i shuffle some cards\n\n")
            stdscr.addstr(y + 0 , x,f"here is your cards:\n\n\nThe {card1} and The {card2}\n\n")
            stdscr.addstr(0 , 0 ,   f"dont bust {totalValue}")

            #hearts
            if cardOne_cards == "Hearts" and cardTwo_cards == "Hearts":
                stdscr.clear()
                stdscr.refresh()
                stdscr.addstr(y - 2 , x ,"Hearts huh?")
                stdscr.addstr(y + 0 , x ,"Dont fall in love kid\n\nbiggest mistake i ever made")
            
            #clubs
            elif cardOne_cards == "Clubs" and cardTwo_cards == "Clubs":
                stdscr.clear()
                stdscr.refresh()
                stdscr.addstr(y - 4 , x ,"See those clubs?")
                stdscr.addstr(y - 2 , x ,"They're like the nights here. No?")
                stdscr.addstr(y + 0 , x ,"Dark, a little rough around the edges,")
                stdscr.addstr(y + 2 , x ,"and you never know what's gonna hit ya.")
                stdscr.addstr(y + 4 , x ,"Just try not to get hit too hard,")
                
            #diamonds
            elif cardOne_cards == "Diamonds" and cardTwo_cards == "Diamonds":
                stdscr.clear()
                stdscr.refresh()
                stdscr.addstr(y - 6 , x ,"See those diamond?")
                stdscr.addstr(y - 4 , x ,"Pretty.\n\n\n\n\n")
                stdscr.addstr(y - 2 , x ,"Probably Worth something.")
                stdscr.addstr(y + 0 , x ,"But you gotta know when to hold 'em, kid.")
                stdscr.addstr(y + 2 , x ,"And more importantly,\nwhen to walk away from 'em.")
                stdscr.addstr(y + 4 , x ,"Learned that the hard way...")
                stdscr.addstr(y + 6 , x ,"a few times...")
                
            
            #spades
            elif cardOne_cards == "Spades" and cardTwo_cards == "Spades":
                stdscr.clear()
                stdscr.refresh()
                stdscr.addstr("spades damn?")
                time.sleep(1)
                stdscr.refresh()
                stdscr.addstr("you wouldnt happen to know any spades do you?\n\n\n\n\n\n")
                stdscr.addstr("some guy named David?")
                stdscr.addstr("No?")
                time.sleep(1)
                stdscr.refresh()
                stdscr.addstr("came in here acting like a total idiot")
                stdscr.addstr("at first it was funny")
                stdscr.addstr("but he ran off with the coins")
                stdscr.addstr("and never tipped the bartenders either")
                stdscr.refresh()
                
            
                 
       
        
        #starting player decisions and dealer banter
        options = ["> 1. thanks\n", 
                   "> 2. youll need the luck\n", 
                   "> 3. just play the fucking game old man\n"]
    
         #this loops through the availble options and prints them to the console
        for i in range(3):
            stdscr.addstr(options[i])
            i = i + 1
    
        #this gets player input for decisoions
        player_input3 = stdscr.getch()
        stdscr.addstr("choose:\n\n")
        if player_input3 == ord('1'):
            stdscr.addstr("you got it\n\n\n")
            stdscr.refresh()
            stdscr.clear()
        elif player_input3 == ord('2'):
            stdscr.addstr("you got guts kid\n\n\n")
            stdscr.refresh()
            stdscr.clear()
        else:
            stdscr.addstr("lifes a game kid, dont rush it\n\n\n")
        
        #this will let the player know the total value
        #then it ask them if they would like to take a hit
        if totalValue <= 5:
            stdscr.addstr(f"Hit? (low risk) at {totalValue} is lucky but 3 more cards will make you a legend")
        if totalValue > 5 and totalValue < 14:
            stdscr.addstr(f"Hit? (low-mid risk) at {totalValue} unless you are super lucky you wont go legendary")
        if totalValue >= 14 and totalValue <= 18:
            stdscr.addstr(f"Hit? (high risk) this is where legends are born")
        if totalValue == 21:
            stdscr.addstr(f"fuck kid, {totalValue}. lets see if this is the legends table ")
    
        #desisions
        choose = ["> 1. Sure"
                , "> 2. Nah"]
        for i in range(2):
            stdscr.addstr(choose[i])
            i = i + 1
            
        player_input4 = stdscr.getch()
        stdscr.addstr("choose:")
        if player_input4 == ord('1'):
            stdscr.refresh()
            stdscr.clear()
            stdscr.addstr("Here:")
            stdscr.addstr(f"{card3}")
            stdscr.addstr(f"alright your at {card1}, {card2}, and {card3}")
        if totalValue > 21:
            stdscr.addstr("you went bust kid\n\n")
            stdscr.addstr("again\n\n")
            options = ["> 1. Yes\n\n", 
                       "> 2. No\n\n"]
            for i in range(2):
                stdscr.addstr(options[i])
                i = i + 1
            
            if player_input4 == ord('1'):
                stdscr.refresh()
                stdscr.clear()
                blackJack()
            else:
                stdscr.addstr("see you again kid")
        else:
            stdscr.refresh()
            stdscr.clear()
            stdscr.addstr("smart\n\n")
            stdscr.addstr(f"so your at {card1} and {card2}\n\n")
            stdscr.addstr(f"while im at {card3} and {card4}")
    
    
    legendStatus = legendStatus + 1
    stdscr.refresh()
    time.sleep(0.1)
    
       
       
       

       
blackJack(stdscr)
wrapper(blackJack)
curses.endwin()

    


# -------------------- Initialization and Teardown --------------------
#import curses
#from curses import wrapper

#stdscr = curses.initscr()  # Initialize the curses screen
#curses.endwin()           # Restore the terminal to its original state

# Using the wrapper (recommended for automatic cleanup)
#def main(stdscr):
    # Your curses code here
    #pass

#if __name__ == '__main__':
    #wrapper(main)

# -------------------- Screen Dimensions --------------------
#height, width = stdscr.getmaxyx()  # Get the height and width of the screen

# -------------------- Basic Output --------------------
#stdscr.addstr(y, x, "String")          # Add a string at position (y, x)
#stdscr.addstr(y, x, "String", attrs)   # Add a string with attributes
#stdscr.clear()                         # Clear the entire screen
#stdscr.refresh()                       # Update the physical screen

# -------------------- Input --------------------
#key = stdscr.getch()                  # Get a single character (int value)
#key_name = curses.keyname(key)        # Get the name of a key (e.g., b'KEY_UP')
#stdscr.nodelay(True/False)           # Non-blocking getch (returns -1 if no input)
#stdscr.timeout(milliseconds)         # getch waits for a specified time
#stdscr.getstr(y, x, n=None)           # Get a string of at most n bytes (or until Enter)

# -------------------- Attributes (for text formatting) --------------------
#curses.A_NORMAL      # Normal display (no attributes)
#curses.A_BOLD        # Bold
#curses.A_DIM         # Half bright
#curses.A_ITALIC       # Italic (may not be supported by all terminals)
#curses.A_UNDERLINE    # Underline
#curses.A_STANDOUT     # Best highlighting mode of the terminal
#curses.A_REVERSE      # Reverse video (swap foreground and background)
#curses.A_BLINK        # Blinking

# Combining attributes with bitwise OR (|)
#stdscr.addstr(y, x, "Bold Text", curses.A_BOLD)
#stdscr.addstr(y, x + 10, "Bold Underline", curses.A_BOLD | curses.A_UNDERLINE)

# -------------------- Colors (requires initialization) --------------------
#curses.start_color()                                # Initialize color support
#curses.has_colors()                                 # Check if the terminal supports colors
#curses.can_change_color()                          # Check if terminal can change color definitions
#curses.init_pair(pair_number, fg_color, bg_color)    # Define a color pair (short int >= 1)
#curses.color_pair(pair_number)                     # Get the attribute for a color pair

# Predefined colors (constants like curses.COLOR_RED, curses.COLOR_GREEN, etc.)
#curses.COLOR_BLACK, curses.COLOR_RED, curses.COLOR_GREEN, curses.COLOR_YELLOW,
#curses.COLOR_BLUE, curses.COLOR_MAGENTA, curses.COLOR_CYAN, curses.COLOR_WHITE

#stdscr.addstr(y, x, "Red on Black", curses.color_pair(1))
#curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

# -------------------- Windows (sub-regions of the screen) --------------------
#subwin = stdscr.subwin(height, width, y, x)   # Create a sub-window
#newwin = curses.newwin(height, width, y, x)   # Create a new window

#win.addstr(...)
#win.refresh()
#win.clear()
#win.border([ls=-1], [rs=-1], [ts=-1], [bs=-1], [tl=-1], [tr=-1], [bl=-1], [br=-1])
# Optional characters for left, right, top, bottom, top-left, top-right, bottom-left, bottom-right corners.
# Use 0 for default border.

#win.keypad(True)                              # Enable special keys for the window
#key = win.getch()
#del win                                       # Delete a window

# -------------------- Special Keys (returned by getch()) --------------------
#curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT
#curses.KEY_ENTER, curses.KEY_BACKSPACE, curses.KEY_TAB
#curses.KEY_HOME, curses.KEY_END, curses.KEY_PAGEUP, curses.KEY_PAGEDOWN
#curses.KEY_RESIZE                              # Terminal resize event

# -------------------- Mouse (requires enabling) --------------------
#curses.mousemask(mask)                       # Set which mouse events to report
                                            # (e.g., curses.BUTTON1_CLICKED)
#curses.getmouse()                           # Get mouse event (returns a tuple)
                                            # (id, x, y, z, bstate)

# Mouse event constants (e.g., curses.BUTTON1_PRESSED, curses.BUTTON_SHIFT)

# -------------------- Panels (for overlapping windows) --------------------
# Requires the curses.panel module (import curses.panel)
# panel = curses.panel.new_panel(win)
# panel.top()
# panel.bottom()
# panel.move(y, x)
# panel.show()
# panel.hide()
# curses.panel.update_panels()
# stdscr.refresh()

# -------------------- Important Notes --------------------
# Always call curses.endwin() to restore the terminal. Using the 'wrapper'
# function handles this automatically.
# Remember to call stdscr.refresh() or win.refresh() after making changes
# to the screen or a window to make them visible.
# Use nodelay(True) with caution, as it can lead to busy-waiting if not handled
# correctly. Consider using timeouts instead for non-blocking input.
# Color support varies between terminals. Always check curses.has_colors().