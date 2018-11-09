from Processes_Module import * 
from Login_New import *
from tkinter import *
#import User_Input_Module 

usernamelist = r"usernamelist.txt" #"tempfile.temp"  
HEADING = "TimesNewRoman 14 bold"
SMALL = "150x150"
NORMAL = "450x400"
BIG = "800x725"

def Signup():  
    global pwordE 
    global nameE
    global rootsignup
 
    rootsignup = Tk() 
    rootsignup.title("Sign Up") 
    rootsignup.geometry(NORMAL)
    intruction = Label(rootsignup, text="Please Enter new Username and password\n", font = HEADING) 
    intruction.place(x=30, y=50) 
 
    nameL = Label(rootsignup, text="New Username: ") 
    pwordL = Label(rootsignup, text="New Password: ") 
    nameL.place(x=70, y=100) 
    pwordL.place(x=73, y=125) 
 
    nameE = Entry(rootsignup) 
    pwordE = Entry(rootsignup, show="*") 
    nameE.place(x=158, y=101) 
    pwordE.place(x=158, y=126) 
 
    signupButton = Button(rootsignup, text="Sign up", command=check_username) 
    signupButton.place(x=158, y=160)
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
    intruction = Label(rootA, text="Please Login\n", font=HEADING) 
    intruction.pack(side=TOP)
    frame1 = Frame(rootA)
    frame1.pack() 
 
    nameL = Label(frame1, text="Username: ") 
    pwordL = Label(frame1, text="Password: ") 
    nameL.grid(row=0, column=0, sticky=E)
    pwordL.grid(row=1, column=0, sticky=E)
 
    nameEL = Entry(frame1) 
    pwordEL = Entry(frame1, show="*")
    nameEL.grid(row=0, column=1, sticky=W)
    pwordEL.grid(row=1, column=1, sticky=W)
    
    loginB = Button(rootA, text="Login", command=to_CheckLogin) 
    loginB.pack()
 
    newsignup = Button(rootA, text="Create new user account", command=New_Signup)
    newsignup.pack()
    
#    rmuser = Button(rootA, text = "Delete User", fg = "red")#, command = DelUser) 
#    rmuser.grid(row=5, columnspan=2, sticky=W)
    
    
    rootA.mainloop()

def to_CheckLogin():
    CheckLogin(nameEL.get(), pwordEL.get())

def to_application():
    r.destroy()
    username = nameEL.get()
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
        loginButton = Button(r, text = "Login again", command = Login_again)
        loginButton.pack(side = LEFT)
        r.mainloop()

def Login_again():
    r.destroy()
    Login()



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

        for F in (Homepage, BMI_Page, Records):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, relheight=1, relwidth=1)
        self.show_frame(Homepage)

        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
        
class Homepage(Frame):  
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
#       label = tk.Label(self, text="Homepage", font=HEADING)
#       label.pack(pady=10,padx=10)
        welcome_text = "Welcome " + nameEL.get()

        heading1 = Label(self, text=welcome_text, font=HEADING)
        heading1.pack() 
        
        BmiButton = Button(self, text="Begin inputting data for BMI", command=lambda : controller.show_frame(BMI_Page))
        BmiButton.pack()
        RecordsButton = Button(self, text="Previous records", command=lambda : controller.show_frame(Records))
        RecordsButton.pack()


class BMI_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.controller = controller
        
        heading = Label(self, text="BMI Calculator", font=HEADING)
        heading.grid(row=0, column=0)
        
#        container = Frame(self)
#        container.pack()

        heightlabel = Label(self, text="Height")
        heightlabel.grid(row=1, column=0)
        masslabel = Label(self, text="Mass")
        masslabel.grid(row=2, column=0)

        heightentry = Entry(self)
        heightentry.grid(row=1, column=1)
        massentry = Entry(self)
        massentry.grid(row=2, column=1)

        calculate_button = Button(self, text="Calculate now")#, command=)
        button.grid(row=3, column=1)
        MenuButton = Button(self, text="Back to menu", command=lambda : controller.show_frame(Homepage))
        MenuButton.grid(row=3, column=1)
        RecordsButton = Button(self, text="Previous records", command=lambda : controller.show_frame(Records))
        RecordsButton.pack()

class Records(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        heading = Label(self, text="Your previous records", font=HEADING)
        heading.pack()

        container = Frame(self)
        container.pack()

        self.message_var = StringVar()
        message = Label(container, textvariable=self.message_var)
        message.grid(row=0, column=0)

        username = nameEL.get()
        filename = format_text(username)
        previous_records = read_records(filename)
        self.message_var.set(previous_records)

        BmiButton = Button(self, text="Begin inputting data for BMI", command=lambda : controller.show_frame(BMI_Page))
        BmiButton.pack()
        MenuButton = Button(self, text="Back to menu", command=lambda : controller.show_frame(Homepage))
        MenuButton.pack()
    
#Processes_Module.Main_window()
