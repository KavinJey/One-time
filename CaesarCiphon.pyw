#Author: Jeyakavin Jeyaranjan

#Purpose: To create and decide One-Time Pads with the use of a key

#Importing Modules
import random

print "\t\tThis is the Beginning of the One-Time-Pad Translator"

x = 0

while x == 0: 
    decision = raw_input("\nWould you like to create or decode?\nRespond with Create or Decode:\n")


    #Start of creating
    if decision == "Create" or decision == "create":
        print 2

        #End loop with setting x either to 0 or not
        
    #Start of decoding and translating
    elif decision=="decode" or decision=="Decode":
        print 2




        #End loop with setting x either to 0 or not
    else:
       print "That is invalid please try again!"
       x = 0 
