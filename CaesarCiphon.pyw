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
key = '-'

#defining functions
#def conversion():
  #  global message_list
 #   message_list = []
    #for character in message:
   #     number = ord(character) - 97
     #   message_list.append(number)
    #print "\n",message_list, "is the alphanumerical order of your message in lowercase"


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
def encryption():
    print "tag1"

def sub_tool(ls):
    z = 0
    while z < len(ls):
        if ls[z] >= 26:
            new_z = ls[z] - 26
            ls.insert(z, new_z)
            ls.pop(z)
            z += 1
            return 
            
        else:
            z += 1
 
while x == 0: 
    decision = raw_input("\nWould you like to create or decode?\nRespond with Create or Decode:\n")


    #Start of Creating the encoded message 
    if decision == "Create" or decision == "create":

        #Getting the message to encrypt
        message = raw_input('Enter the message you would like to encrypt with no spaces or special characters:\n')
        message = message.lower()
        conversion(message)
        message_alphaNum = conversion(message)
        print "\n",message_alphaNum, "is the alphanumerical order of your message in lowercase"

        #Giving user the Key
        key = key_generate()
        print "Your key is: ", key
        conversion(key)
        key_alphaNum = conversion(key)
        print key_alphaNum, "is the alphanumerical order of your key in lowercase"

        #Adding both alpha_Nums
        encrypted_M = [x + y for x, y in zip(message_alphaNum, key_alphaNum)]
        print "Message + key has", encrypted_M, "as its alphanumerical."

        
        if condition(encrypted_M) == False:
            encryption()

        else:
            sub_tool(encrypted_M)
        
        x = x + 1

        #End loop with setting x either to 0 or not
        
    #Start of decoding and translating
    elif decision=="decode" or decision=="Decode":
        print 2




    #End loop with setting x either to 0 or not
    else:
       print "That is invalid please try again!"
       x = 0 
