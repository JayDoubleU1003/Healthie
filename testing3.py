from tkinter import *
from Processes_Module import *
from Login_New import *

class A(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.result = StringVar()
        self.results = Label(self, textvariable=self.result)
        self.results.grid(row=0, column=0)

        button = Button(self, text="Click me", command=self.test)
        button.grid(row=1, column=0)

        self.result.set("This is not a text")

    def test(self):
        filename = format_text("hello")
        self.result.set(read_records(filename))

root = Tk()
app = A(root)
app.pack()
root.mainloop()
