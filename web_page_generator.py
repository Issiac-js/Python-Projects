import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #title
        self.master.title("Web Page Generator")
        #button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=3, padx=(10,10), pady=(10,10))

        #label
        self.l1 = Label(self.master, text='Enter Custom text or click the Default HTML page button')
        self.l1.grid(row=1, column=1, columnspan=2,  padx=(10,10), pady=(10,10))
        #entry
        self.e = Entry(width=130)
        self.e.grid(row=2, column=1, columnspan=4, pady=(10,10))

        #another Button
        self.custombtn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custombtn.grid(row=3, column=4, padx=(10,10), pady=(10,10))


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = self.e.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
