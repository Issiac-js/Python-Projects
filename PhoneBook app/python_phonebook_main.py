"""

A phone book aplication using Tkinter

"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Import other modules in order to access them
import python_phonebook_func
import python_phonebook_gui



#Frame is the Tkinter class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        #define our master frame configuartion
        self.master = master
        self.master.minsize(500,300) #(height,width)
        self.master.maxsize(500,300)

        #This CenterWindow method will center our app on the user's screen
        python_phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.config(bg="#F0F0F0")

        #This protocol method is bult-in method to catch if the user clicks the 'X' in the upper corner
        self.master.protocol("WM_DELETE_WINDOW", lambda: python_phonebook_func.ask_quit(self))
        arg = self.master


        # load in the GUI widgets from a seprate module keeping the code compartmenalized.
        python_phonebook_gui.load_gui(self)


        #Instantiate the Tkinter menu dropdown object
        #This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: python_phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) #defines the particular drop down column and tearoff=0 means do not sperate from menu
        helpmenu.add_seperator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") #add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu)#add_cascade is a parent menubar item (visible heading)


        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional
            funtionality or appearances such as boarderwidth.

        """

        self.master.config(menu=menubar, boarderwidth='1')

        if __name__ =="__main__":
            root = tk.Tk()
            App = ParentWindow(root)
            root.mainloop()












        
