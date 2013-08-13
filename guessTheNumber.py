# Guess the Number
# This game can be played @ the following url
# http://www.codeskulptor.org/#user11_HvxdNumfsY_2.py

import random
import math
import simplegui


# initialize global variables used in your code


secret_number = 0
guess_limit = 0
game = ''




# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    global guess_limit
    global game
    game = 1
    secret_number = random.randrange(0, 101)
    guess_limit = 7
    print("\r\n")
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is ", guess_limit

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    global guess_limit
    global game
    game = 0
    secret_number = random.randrange(0, 1001)
    guess_limit = 10
    print("\r\n")
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is ", guess_limit

def get_input(guess):
    # main game logic goes here
    global secret_number
    global guess_limit
    global game
    guess = int(guess)
    guess_limit -= 1
    print("\r\n")
    print "Guess was ", guess
    print "Number of remaining guesses is ", guess_limit
    if secret_number < guess:
        print "Lower!"        
    elif secret_number > guess:
        print "Higher!"
    else:
        print "Correct!"
        if game:
            range100()
        else:
            range1000()
    if guess_limit <= 0:
        print "Out of guesses."
        print "You Lose! Good Day Sir!"		
        if game:
            range100()
        else:
            range1000()
    
        
# create frame
f = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# start frame
f.start()