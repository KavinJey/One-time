from Tkinter import *
import Tkinter
import random
import string
from random import choice
from string import ascii_lowercase

top = Tkinter.Tk()
x = 0

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
        if p < 0:
            new_p = p + 26
            ls[count] = new_p
            count += 1
        else:
            count += 1


def create():
    create.config(state="disabled")
    #Creating new window
    top = Tk()

    #Displaying information on text
    L1 = Label(top, text="""Welcome to creating a one-time pad, this little app\nallows one to encode their messages with one of the\nmost secure versions of encryption known to man,
    with only a key as well as a encrypted message\nyou can send secret messages to anyone.

    Enter your message with no spaces or special characters
    below.

    """)
    L1.pack(side = TOP)

    
    message = StringVar()
    L2 = Label(top, text="Enter Message: ")
    L2.pack(side = LEFT)
    Entry1 = Entry(top, textvariable=message)
    Entry1.pack(side = LEFT)
    

    def getMessage():
        #Opens new window
        top = Tk()
        
        #Does all the math for the encryption as well as generating a key
        message = Entry1.get()
        message = message.lower()
        conversion(message)
        message_alphaNum = conversion(message)

        key = key_generate()
        conversion(key)
        key_alphaNum = conversion(key)
        encrypted_M = [x + y for x, y in zip(message_alphaNum, key_alphaNum)]

        #Using Sub_tool function to change values if >=26
        sub_tool(encrypted_M)

        alpha_Conversion(encrypted_M)
        encrypted_M = str(encrypted_M).translate(None, "[ ] ' ,")
        
        

        T1 = Text(top)
        T1.insert(INSERT, "Your message is: ")
        T1.insert(INSERT, message)

        T1.insert(INSERT, "\n\nYour encoded message is: ")
        T1.insert(INSERT, encrypted_M)
        
        T1.insert(INSERT, "\n\nYour key is: ")
        T1.insert(INSERT, key)
        
        T1.pack()
        top.mainloop()
       
    B1 = Button(top, text="Enter", width=15, command=getMessage)
    B1.pack() 


    print message
    top.mainloop()

     
def decode():
    decode.config(state="disabled")
    
    #Creating new window
    top = Tk()

    #Displaying information on text
    L1 = Label(top, text="\t\t\tHere you can decode your message. \n")
    L1.grid()

    
    message = StringVar()
    key = StringVar()
    
    L2 = Label(top, text="Enter Encrypted Message: ")
    L2.grid(column=0)
    
    L3 = Label(top, text="Enter key: ")
    L3.grid(column = 0)
    
    Entry1 = Entry(top, textvariable=message)
    Entry1.grid(column = 1, row = 1)
    

    
    Entry2 = Entry(top, textvariable=key)
    Entry2.grid(column = 1, row = 2)
    

    def getDecode():
        top = Tk()
        
        #Getting key and message
        e_message = Entry1.get()
        e_message = e_message.lower()
        key = Entry2.get()
        key = key.lower()
        

        #Converting key and message into place in alpha_Num
        key = conversion(key) 
        e_message = conversion(e_message)

        if len(key) == len(e_message):
            
            #Adding both lists 
            new_message = [x - y for x, y in zip(e_message, key)]
            add_tool(new_message)
            
            #Converting number list into alphabets
            alpha_Conversion(new_message)
            
            new_message = str(new_message).translate(None, "[ ] ' ,")

            T1 = Text(top)
            T1.insert(INSERT, "Your key is: ")
            T1.insert(INSERT, key)

            T1.insert(INSERT, "\n\nYour encoded message is: ")
            T1.insert(INSERT, e_message)
        
            T1.insert(INSERT, "\n\nYour message is: ")
            T1.insert(INSERT, new_message)
        
            T1.pack()
            top.mainloop()
       
            

        else:
            T1 = Text(top)
            T1.insert(INSERT, "Your key and message must be the same length try again!")

            
    B1 = Button(top, text="Enter", width=15, command=getDecode)
    B1.grid(column = 1, row = 3)
    
    
#Buttons that make it all work 
create = Tkinter.Button(text = "Create", command = create, width = 15)

decode = Tkinter.Button(text = "Decode", command = decode, width = 15)
create.pack(side = LEFT)
decode.pack(side = RIGHT)

top.mainloop()

