from Tkinter import *
import Tkinter

top = Tkinter.Tk()
frame = Frame(top)
frame.pack()

def create():
    #Creating new window
    top = Tk()

    #Displaying information on text
    L1 = Label(top, text="""Welcome to creating a one-time pad, this little app
    allows one to encode their messages with one of the
    most secure versions of encryption known to man,
    with only a key as well as a encrypted message
    you can send secret messages to anyone.

    Enter your message with no spaces or special characters
    below.

    """)
    L1.pack(side = TOP)

    
    message = ""
    L2 = Label(top, text="Enter Message: ")
    L2.pack(side = LEFT)
    Entry1 = Entry(top, textvariable=message)
    Entry1.pack(side = RIGHT)
    Entry1.get()


    
    top.mainloop()
    
create = Tkinter.Button(text = "Create", command = create, width = 15)

create.pack()

top.mainloop()
