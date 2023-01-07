"""
This program transfers files and will also be able to detect and transfer files that were recently modified or new within 24hrs

"""
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import date
import time


class ParentWindow(Frame):


    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI Window
        self.master.title("File Transfer")

        #creates button to select file from directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Position source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Position entry in GUI and line it up with the button
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #creates button for destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Position d button on row under source Button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #creates entry for destination directory
        self.destination_dir = Entry(width=75)
        #Position in GUI with Button
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Position transfer Button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0,15))

        #create an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Position exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))


        #create function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END ) will clear the content that is inserted in the entry widgeth
            #This allows the path to be inserted into the Entry Widget properly.
        self.source_dir.delete(0, END)
        # the .insert method will insert the user selection to the source_dir Entry.
        self.source_dir.insert(0, selectSourceDir)


    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END ) will clear the content that is inserted in the entry widgeth
            #This allows the path to be inserted into the Entry Widget properly.
        self.destination_dir.delete(0, END)
        # the .insert method will insert the user selection to the destination_dir Entry.
        self.destination_dir.insert(0, selectDestDir)


    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory
        for i in source_files:

            path = (source + '/' + i)
            #get current time in seconds
            currentTime = time.time()
            #gets the last time file was edited in seconds
            fileTime = os.path.getmtime(path)
            #this gets the difference in time
            difference_in_time = currentTime - fileTime
            #this changes the seconds to minutes
            seconds_to_minutes = difference_in_time / 60
            #this changes the minutes to hours
            minutes_to_hours = seconds_to_minutes / 60
            #this changes it from a float to an integer
            hours = int(minutes_to_hours)

            #moves each file from the source to destination if hours is less then 24hrs from currentTime
            if hours < 24:
                shutil.move(source + '/' + i, destination)
                print(i + " was successfully transferred.")
            else:
                print("File:", i, "was not moved.")


    #create function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
