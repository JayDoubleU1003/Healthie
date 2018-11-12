from tkinter import *
from Processes_Module import *
from Login_New import *

root = Tk()

result = StringVar()
results = Label(root, textvariable=result)
results.grid()
 
filename = format_text("hello")
result.set(read_records(filename))
root.mainloop()
