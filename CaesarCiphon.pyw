#Author: Jeyakavin Jeyaranjan

#Purpose: To create and decide One-Time Pads with the use of a key

#Importing Modules
import random
import string
from random import choice
from string import ascii_lowercase



print "This is the Beginning of the One-Time-Pad Translator. This is the world's safest way of encryption. \nJust give the message and the key to the receiving persons and they",
print "and only they can decode your message. "


#Sentry Variables
x = 0
amount_letters = 0
key = '-'

#Defining functions

def conversion(message):
    global message_list
    message_list = []
    for character in message:
        number = ord(character) - 97
        message_list.append(number)
    
    return message_list

    
def key_generate():
    len(message_list)
    return ''.join(random.choice(ascii_lowercase) for i in range(len(message_list)))

def condition(ls):
    for p in ls:
        if p >= 26:
            return True
    return False

#Converts Message into letters again
def alpha_Conversion(ls):
    count = 0
    for x in ls:
        new_x = x + 97
        new_x = chr(new_x)
        ls[count] = new_x
        count += 1
        

def sub_tool(ls):
   count = 0 
   for p in ls:     
        if p >= 26:
            new_p = p - 26
            ls[count] = new_p
            count += 1     
        else:
            count += 1

def add_tool(ls):
    count = 0
    for p in ls:
        if p <= 0:
            new_p = p + 26
            ls[count] = new_p
            count += 1
        else:
            count += 1
            
#START OF PROGRAM
            
while x == 0: 
    decision = raw_input("\nWould you like to create or decode?\nRespond with Create or Decode:\n")


    #Start of Creating the encoded message 
    if decision == "Create" or decision == "create":

        #Getting the message to encrypt
        message = raw_input('Enter the message you would like to encrypt with no spaces or special characters:\n')
        message = message.lower()
        conversion(message)
        message_alphaNum = conversion(message)

        #Giving user the Key
        key = key_generate()
        print "\nYour key is: ", key, 
        conversion(key)
        key_alphaNum = conversion(key)

        #Adding both alpha_Nums
        encrypted_M = [x + y for x, y in zip(message_alphaNum, key_alphaNum)]
        
        #Using Sub_tool function to change values if >=26
        sub_tool(encrypted_M)
        
    
        print "\n\nEncrypting...\n"
        alpha_Conversion(encrypted_M)

        print "Your encrypted message is: ",
        print str(encrypted_M).translate(None, "[ ] ' ,")
        print "With the key:", key

        
        x = x + 1

        #End loop with setting x either to 0 or not


        
    #Start of decoding and translating
    elif decision=="decode" or decision=="Decode":

        #Getting key and message
        key = raw_input("Enter your key:\n")
        key = key.lower()
        e_message = raw_input("Enter your message:\n")
        e_message = e_message.lower()

        #Converting key and message into place in alpha_Num
        key = conversion(key) 
        e_message = conversion(e_message)

        if len(key) == len(e_message):
            #Adding both lists 
            new_message = [x - y for x, y in zip(e_message, key)]
            add_tool(new_message)
            print new_message
            #Converting number list into alphabets
            alpha_Conversion(new_message)
            print "Your new message is: "
            print str(new_message).translate(None, "[ ] ' ,")
            

        else:
            print "Error, Key and Message must be same length"
        
        
        x = x + 1


    #End loop with setting x either to 0 or not
    else:
       print "That is invalid please try again!"
       x = 0 
