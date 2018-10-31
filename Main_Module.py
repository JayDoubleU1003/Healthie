from Processes_Module import * 
from Login_New import *
from tkinter import *
#import User_Input_Module 

usernamelist = r"usernamelist.txt" #"tempfile.temp"  
HEADING = "TimesNewRoman 12 bold"
SMALL = "150x150"
NORMAL = "400x400"
BIG = "800x725"

def Signup():  
    global pwordE 
    global nameE
    global rootsignup
 
    rootsignup = Tk() 
    rootsignup.title("Sign Up") 
    rootsignup.geometry(NORMAL)
    intruction = Label(rootsignup, text="Please Enter new Username and password\n", font = HEADING) 
    intruction.grid(row=0, columnspan=5,) 
 
    nameL = Label(rootsignup, text="New Username: ") 
    pwordL = Label(rootsignup, text="New Password: ") 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(rootsignup) 
    pwordE = Entry(rootsignup, show="*") 
    nameE.grid(row=1, column=1, sticky = W) 
    pwordE.grid(row=2, column=1, sticky = W) 
 
    signupButton = Button(rootsignup, text="Sign up", command=check_username) 
    signupButton.grid(columnspan=2, sticky=W)
    rootsignup.mainloop()

def check_username():
    newusername = nameE.get()
    existing_accounts = check_file(usernamelist)
    create = True

    for account in existing_accounts:
        if newusername == account["Username"]:
            create = False
            print("Username has been taken")
            break
        else:
            continue
        
    if create:
        add_new_user(nameE.get(), pwordE.get())
        usersavefile = format_text(newusername)
        create_file(usersavefile)
        rootsignup.destroy() 
        Login() 
  
    else:
        signupagain = Tk() #creates a new window when sign up informations are not provided. 
        signupagain.title("Signup failed")
        signup_fail = Label(signupagain, text = "Please fill in required info\n", fg = "red")
        signupagain.geometry(SMALL)
        signup_fail.pack()
            
        signupa_B = Button(signupagain, text = "Sign up again", command = signupagain.destroy)
        signupa_B.pack()
            
        signupagain.mainloop()

def Login():
    global nameEL
    global pwordEL 
    global rootA

    rootA = Tk() 
    rootA.title("Login") 
    rootA.geometry(NORMAL)
    intruction = Label(rootA, text="Please Login\n") 
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text="Username: ") 
    pwordL = Label(rootA, text="Password: ") 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show="*")
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
    
    loginB = Button(rootA, text="Login", command=to_CheckLogin) 
    loginB.grid(row=3, sticky=W)#,columnspan=2)
 
    newsignup = Button(rootA, text="Create new user account", command=New_Signup)
    newsignup.grid(row=4, sticky=W, columnspan=2)
    
#    rmuser = Button(rootA, text = "Delete User", fg = "red")#, command = DelUser) 
#    rmuser.grid(row=5, columnspan=2, sticky=W)
    
    
    rootA.mainloop()

def to_CheckLogin():
    CheckLogin(nameEL.get(), pwordEL.get())

def to_application():
    username = nameEL.get()
    r.destroy()
    Application(username).mainloop()

def CheckLogin(nameEL, pwordEL):
    global r
    
    authorized = login(nameEL, pwordEL)
    username = nameEL  

    if authorized:
            r = Tk() 
            r.title("XD")
            r.geometry(SMALL) 
            rlbl = Label(r, text = "\n[+] Logged In") 
            rlbl.pack()
            continue_Button = Button(r, text = "Continue into app", command = to_application)#, command = Processes_Module.Main_window) 
            continue_Button.pack()
            r.mainloop()
        
    else:
        rootA.destroy()
        r = Tk()
        r.title("D:")
        r.geometry(SMALL)
        rlbl = Label(r, text="\n[!] Invalid Login")
        rlbl.pack()
        loginButton = Button(r, text = "Login again", command = Login)
        loginButton.pack(side = LEFT)
        r.mainloop()

def New_Signup():
    rootA.destroy()
    Signup()

class Application(Tk):
    def __init__(self, user):
        Tk.__init__(self)

        self.title("Healthie")
        self.geometry(BIG)
        self.user = user

        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        self.frames = {}

        for F in (Homepage, BMI_Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Homepage)

        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
  
        
class Homepage(Frame):  

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

#       label = tk.Label(self, text="Homepage", font=HEADING)
#       label.pack(pady=10,padx=10)
        welcome_text = "Welcome " + nameEL.get()
        heading1 = Label(self, text = welcome_text, font = HEADING)
        heading1.pack() 
        
        BmiButton = Button(self, text = "Begin inputting data for BMI", command = lambda : controller.show_frame(BMI_Page))
        BmiButton.pack()


class BMI_Page(Frame):

    def __init___(self, parent, controller):
        Frame.__init__(self, parent)
        heading = Label(self, text = "BMI Calculator", font = HEADING)
        heading.grid(row = 0, columnspan = 3, sticky = E)

        heightlabel = Label(self, text = "Height")
        heightlabel.grid(row = 2, column = 0)

        masslabel = Label(self, text = "Mass")
        masslabel.grid(row = 3, column = 0)



        



try:
    check_file(usernamelist)
    Login()   
except:
    create_file(usernamelist)
    Signup()
    
#Processes_Module.Main_window()
