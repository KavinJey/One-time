#Author: Jeyakavin Jeyaranjan

#Purpose: To create and decide One-Time Pads with the use of a key

#Importing Modules
import random
from random import choice
from string import ascii_lowercase 

print "\t\tThis is the Beginning of the One-Time-Pad Translator"


#Sentry Variables
x = 0
amount_letters = 0
key = ""


#defining functions
def conversion():
    message = raw_input('Enter the message you would like to encrypt with no spaces or special characters:\n')
    message = message.lower()
    global output
    output = []
    for character in message:
        number = ord(character) - 97
        output.append(number)
    print "\n",output, "is the alphanumerical order of your message in lowercase"
    
def key_generate():
    len(output)
    print(''.join(choice(ascii_lowercase) for n in range(len(output)))), "is your key"

    
while x == 0: 
    decision = raw_input("\nWould you like to create or decode?\nRespond with Create or Decode:\n")


    #Start of creating
    if decision == "Create" or decision == "create":
        conversion()
        key_generate()

        
        x = x + 1

        #End loop with setting x either to 0 or not
        
    #Start of decoding and translating
    elif decision=="decode" or decision=="Decode":
        print 2




    #End loop with setting x either to 0 or not
    else:
       print "That is invalid please try again!"
       x = 0 
