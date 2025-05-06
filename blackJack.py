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
def topRight(stdscr, text , color_attr = 1 ):
    height, width = stdscr.getmaxyx()
    #cutting the text at the end so it doesnt wrap the terminal
    if len(text) > width:
        #this specificallly cuts it to 1 line
        text = text[:width] 
    #this minuses the width by the length of the text so we get the full wdth minus the text length
    x = width - len(text) 
    stdscr.attron( color_attr )
    stdscr.addstr( 0 , x , text )
    stdscr.attroff( color_attr )
    stdscr.refresh()
    
#displays text at the bottom right
def bottomRight(stdscr, text , color_attr = 0 ):
    height, width = stdscr.getmaxyx()
    if len(text) > width:
        #this specificallly cuts it to 1 line
        text = text[:width] 
    #this minuses the width by the length of the text so we get the full wdth minus the text length
    x = width - len(text)
    y = height - 1
    stdscr.addstr(y , x , text)
    stdscr.refresh()
    
#displays text at the bottom left of the screen.
def bottomLeft(stdscr, text):
    height, width = stdscr.getmaxyx()
    if len(text) > width:
        text = text[:width]
    y = height - 1
    stdscr.addstr(y , 0 , text)
    stdscr.refresh()
    
#displays text at the top left of the screen
def topLeft(stdscr,text):
    height, width = stdscr.getmaxyx()
    if len(text) > width:
        text = text[:width]
    y = height - height # + 1
    x = width - width # + 1
    stdscr.addstr(y , x , text)
    stdscr.refresh()
    
#this function will center arrays of text.
#very useful when writing tons of scripts that need to be called.
def centerText(stdscr,strings , color1):
    height , width = stdscr.getmaxyx()
    num_strings = len(strings)
    
    starting_y = (height - num_strings) // 2
    
    #loop to print our text out
    for i, text in enumerate(strings):
        x =  (width - len(text)) // 2
        y = starting_y + i
        if len(text) > width:
            text = text[:width]
        
        #only works if using an array
        stdscr.attron(color1)
        stdscr.addstr( y , x , text )
        stdscr.attroff(color1)
        stdscr.refresh()
    stdscr.refresh()
    
    
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
    
#this is the values section where we will add the cards.
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

def risk(stdscr, total):
    if 2 <= total <= 10:
        risk_level = "low"
    elif 11 <= total <= 16:
        risk_level = "medium"
    elif total >= 17:
        risk_level = "high"
    else:
        risk_level = "none"
    riskString = (f"Risk: {risk_level}")
    topLeft(stdscr, riskString)
    stdscr.refresh()


#main game funtion
def blackJack(stdscr , color1 , color2 , color3):
    legendStatus = 0
    legend = 0
    player_choice = None
    
    while legendStatus < 100:
        
        #this section is the welcome screen, explaining the rules
        stdscr.clear()
        stdscr.refresh()
        strings = ["Welcome to the BlackJack Table!" , 
                   "The rules are simple:" , 
                   "(__First to 21 wins__)" , 
                   "(__First round is on the house__)" , 
                   "(__First to bust pays for drinks 😁__)" , 
                   "Press 1 to continue"
                   ]
        
        centerText( stdscr , strings , color1 )
        stdscr.refresh()
        
        #this gets player input
        player_choice = stdscr.getch()
        if player_choice == ord('1'): 
            stdscr.clear()
            stdscr.refresh() 
            strings = ["Take a seat while i shuffle some cards" ,
                       "here is your cards:" ,
                       f"The {card1} and The {card2}" ,
                        "Press 1 to continue"
                       ]
            score = ( f"Total : {totalValue}" )
            centerText(stdscr , strings , color1)
            topRight( stdscr , score )
            risk(stdscr , totalValue)
            stdscr.refresh()

            #hearts
            if cardOne_cards == "Hearts" and cardTwo_cards == "Hearts":
                stdscr.clear()
                stdscr.refresh()
                text1 = [ "Hearts huh?" ,
                         "Dont fall in love kid" ,
                         "biggest mistake i ever made" 
                        ]
                centerText( stdscr , text1 , color1)
                score = ( f"Dont Bust : {totalValue}" )
                bottomLeft( stdscr , score )
                risk( stdscr , totalValue )
                stdscr.refresh()
                
            
            #clubs
            elif cardOne_cards == "Clubs" and cardTwo_cards == "Clubs":
                stdscr.clear()
                stdscr.refresh()
                text2 = [ "See those clubs?" ,
                            "They're like the nights here. No?" ,
                            "Dark? a little rough around the edges?" ,
                            "and you never know what's gonna hit ya." ,
                            "Just try not to get hit too hard." 
                          ]
                
                score = ( f"Dont Bust : {totalValue}" )
                centerText( stdscr , text2 , color1 ) 
                bottomLeft(stdscr , score)
                risk( stdscr , totalValue )
                
            #diamonds
            elif cardOne_cards == "Diamonds" and cardTwo_cards == "Diamonds":
                stdscr.clear()
                stdscr.refresh()
                text3 = ["See those diamond?" ,
                           "Pretty?" ,
                           "Probably Worth something." ,
                           "But you gotta know when to hold 'em, kid." ,
                           "And more importantly, when to walk away from 'em." ,
                           "Learned that the hard way..." ,
                           "a few times..."
                           ]
                score = ( f"Total : {totalValue}" )
                centerText( stdscr , text3 , color1 )
                bottomLeft(stdscr , score )
                risk( stdscr , totalValue )
            
            #spades
            elif cardOne_cards == "Spades" and cardTwo_cards == "Spades":
                stdscr.clear()
                stdscr.refresh()
                text4 = ["spades damn?" ,
                           "you wouldnt happen to know any spades do you?" ,
                           "some guy named David?" ,
                           "No?" ,
                           "came in here acting like a total idiot" ,
                           "at first it was funny" ,
                           "but he ran off with the coins" ,
                           "and never tipped the bartenders either" ,
                           ]
                centerText( stdscr , text4 , color1)
                score = ( f"Total : {totalValue}" )
                bottomLeft( stdscr , score )
                risk( stdscr , totalValue )
                stdscr.refresh()
        
    
        player_choice = stdscr.getch()
        if player_choice == ord('1'):
            stdscr.clear()
            stdscr.refresh()
            string1 = [f"would you like a hit?" , 
                      f"So far you have The {card1}, The {card2}",
                      "1. Yes " ,
                      "2. No"]
            centerText( stdscr, string1 , color1 )
            risk( stdscr , totalValue )
            stdscr.refresh()
            player_choice = stdscr.getch()
            if player_choice == ord('1') and totalValue < 21:
                stdscr.clear()
                stdscr.refresh()
                string2 = [f"you have The {card1} The {card2} and The {card3}" ,
                            "would you like another hit" ,
                            "1 .Yes" ,
                            "2 .No"]
                centerText( stdscr , string2 , color1 )
                risk( stdscr , firstHitValue )
                stdscr.refresh()
                if player_choice == ord('1') and firstHitValue < 21:
                    stdscr.clear()
                    stdscr.refresh()
                    string3 = ["you are now entering legendary mode" ,
                               "taking another hit will boost legendary status if you dont bust" ,
                               "would you like a hit?" ,
                               "you always run the risk of losing" ,
                               "if you only think about winning there is no risk - me" , 
                               "1 .Yes" ,
                               "2 .No"
                               ]
                    centerText(stdscr , string3 , color2)
                    if player_choice == ord('1'):
                        stdscr.clear()
                        stdscr.refresh()
                        
                elif firstHitValue > 21:  
                    string5 = ["busted dawg" ,
                               "try not to be a loser" ,
                               "play again and not suck? #skill issue"
                               "1 .Yes , ill get my ass handed to me again like a good boi" ,
                               "2 .No , because i always give up on everything - you probably"]
                         

            else:
                stdscr.clear()
                stdscr.refresh()
                string3 = [f"you have The {card1} and The {card2}"]
                centerText( stdscr , string3 , color1)
                stdscr.refresh()
        
        
        
    
    legendStatus += 1
    stdscr.refresh()
    
def main(stdscr):
    if curses.has_colors():
        curses.start_color()
        
        #ill match the colors better later
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        
        #color pairs
        color1 = curses.color_pair(1)
        color2 = curses.color_pair(2)
        color3 = curses.color_pair(3)
        
        #changes background color
        stdscr.bkgd(' ', color3 )
        stdscr.clear()
        stdscr.refresh()
        
        #adds are colors are parameters but literally makes them global so we can use them
        blackJack( stdscr , color1 , color2 , color3 )
    else:
        blackJack( stdscr , 0 , 0 , 0)
        
if __name__ == '__main__':
    wrapper(main)


    


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