from tkinter import *
import os
import Processes_Module

creds = "tempfile.temp" 
HEADING = "TimesNewRoman 12 bold"
SIZE = "400x400"

def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global rootsignup
 
    rootsignup = Tk() # This creates the window, just a blank one.
    rootsignup.title("Sign Up") # This renames the title of said window to 'signup'
    rootsignup.geometry(SIZE)
    intruction = Label(rootsignup, text="Please Enter new Username and password\n", font = HEADING) # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, columnspan=5,) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(rootsignup, text="New Username: ") # This just does the same as above, instead with the text new username.
    pwordL = Label(rootsignup, text="New Password: ") # ^^
    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W) # ^^
 
    nameE = Entry(rootsignup) # This now puts a text box waiting for input.
    pwordE = Entry(rootsignup, show="*") # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1, sticky = W) # You know what this does now :D
    pwordE.grid(row=2, column=1, sticky = W) # ^^
 
    signupButton = Button(rootsignup, text="Sign up", command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    rootsignup.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():
  if nameE.get() != "" and pwordE.get() != "":   
      with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
            f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
            f.write('\n') # Splits the line so both variables are on different lines.
            f.write(pwordE.get()) # Same as nameE just with pword var
            f.close() # Closes the file
    
            rootsignup.destroy() # This will destroy the signup window. :)
            Login() # This will move us onto the login definition :D
  
  else:
      signupagain = Tk() #creates a new window when sign up informations are not provided. 
      signupagain.title("Signup failed")
      signup_fail = Label(signupagain, text = "Please fill in required info\n", fg = "red")
      signupagain.geometry(SIZE)
      signup_fail.pack()
      
      signupa_B = Button(signupagain, text = "Sign up again", command = signupagain.destroy)
      signupa_B.pack()
      
      signupagain.mainloop()
    
 
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title("Login") # This makes the window title 'login'
    rootA.geometry(SIZE)
    intruction = Label(rootA, text="Please Login\n") # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text="Username: ") # More labels
    pwordL = Label(rootA, text="Password: ") # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
    
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    global r
    
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        r = Tk() # Opens new window
        r.title("XD")
        r.geometry(SIZE) # Makes the window a certain size
        rlbl = Label(r, text = "\n[+] Logged In") # "logged in" label
        rlbl.pack()
        continue_Button = Button(r, text = "Continue into app", command = Processes_Module.Main_window) 
        continue_Button.pack()
        r.mainloop()
        
    else:
        r = Tk()
        r.title("D:")
        r.geometry(SIZE)
        rlbl = Label(r, text="\n[!] Invalid Login")
        rlbl.pack()
        r.mainloop()
 
def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
 
#if os.path.isfile(creds):
#    Login()
#else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
#    Signup()
