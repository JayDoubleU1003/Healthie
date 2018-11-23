from Processes_Module import * 
from Login_Module import *
from tkinter import *
import os
import datetime

#the followings are some fixed value that would be used by the GUI
usernamelist = r"usernamelist.txt"  
HEADING = "TimesNewRoman 14 bold"
SMALL = "150x150+450+250"
NORMAL = "525x400+450+250"

#the following code creates a signup window
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

#the function checks the entries before creating a new account
def check_username():
    newusername = nameE.get()  
    newpassword = pwordE.get()
    existing_accounts = check_file(usernamelist)
    create = True

    for account in existing_accounts: 
        if newusername == account["Username"]:  #checks availability of username
            create = False
            error = Tk()
            error.title("Signup failed")
            usernametakenL = Label(error, text="Username has been taken\n", fg="red")
            usernametakenL.pack()
                
            signupa_B = Button(error, text="Sign up again", command=error.destroy)
            signupa_B.pack()
                
            break
        else:
            continue
            
    if newusername == "" or newpassword == "":  
        signupagain = Tk()  
        signupagain.title("Signup failed")
        signup_fail = Label(signupagain, text="Please fill in required info\n", fg="red")
        signupagain.geometry(SMALL)
        signup_fail.pack()
                    
        signupa_B = Button(signupagain, text="Sign up again", command=signupagain.destroy)
        signupa_B.pack()
                    
        signupagain.mainloop()
    
    elif create:
        add_new_user(newusername, newpassword)
        usersavefile = format_text(newusername)
        create_save_file(usersavefile)
        rootsignup.destroy() 
        Login() 


def Login():    #creates login page
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
    
    rootA.mainloop()

def to_CheckLogin():
    CheckLogin(nameEL.get(), pwordEL.get())

def to_application(username):
    Application(username)

def CheckLogin(nameEL, pwordEL):

    authorized = login(nameEL, pwordEL) #checks login info given
    username = nameEL  

    if authorized:
        to_application(username)
        
    else:
        rootA.destroy()
        r = Tk()
        r.title("D:")
        r.geometry(SMALL)
        rlbl = Label(r, text="\n[!] Invalid Login")
        rlbl.pack()
        loginButton = Button(r, text = "Login again", command = lambda:Login_again(r))
        loginButton.pack()
        r.mainloop()

def Login_again(r):
    r.destroy()
    Login()


def New_Signup():
    rootA.destroy()
    Signup()


#the following function for the application which consists of 3 separate pages. 
def Application(username):
    global Homepage
    global Bpage
    global Rpage
    
    App = Tk()
    App.withdraw() #hides the main window
    user = username

    Homepage = Toplevel(App)

    Homepage.title("Healthie")
    Homepage.geometry(NORMAL)
    
    welcome_text = "Welcome \"" + user + "\""

    heading1 = Label(Homepage, text=welcome_text, font=HEADING)
    heading1.pack()
    
    Hcontainer = Frame(Homepage)
    Hcontainer.pack()
    
    BmiButton = Button(Hcontainer, text="Begin inputting data for BMI and blood pressure", command=to_BMI_Page)
    BmiButton.grid()
    RecordsButton = Button(Hcontainer, text="Previous records", command=to_Records_Page)
    RecordsButton.grid()
    QuitButton = Button(Hcontainer, text="Quit Program", command=lambda : quit_application(App))
    QuitButton.grid()

###########################################page separator###########################################################################
    
    Bpage = Toplevel(App) 

    Bpage.title("Healthie")
    Bpage.geometry(NORMAL)
    
    heading = Label(Bpage, text="BMI & Blood pressure", font=HEADING)
    heading.pack()
        
    Bcontainer = Frame(Bpage)
    Bcontainer.pack()

    heightlabel = Label(Bcontainer, text="Height (in m)")
    heightlabel.grid(row=0, column=0)
    masslabel = Label(Bcontainer, text="Mass (in Kg)")
    masslabel.grid(row=1, column=0)
    sbp_label = Label(Bcontainer, text="Blood pressure(Systolic)")
    sbp_label.grid(row=2, column=0)
    dbp_label = Label(Bcontainer, text="Blood pressure(Diastolic)")
    dbp_label.grid(row=3, column=0)

    heightentry = Entry(Bcontainer)
    heightentry.grid(row=0, column=1)
    massentry = Entry(Bcontainer)
    massentry.grid(row=1, column=1)
    sbp_entry = Entry(Bcontainer)
    sbp_entry.grid(row=2, column=1)
    dbp_entry = Entry(Bcontainer)
    dbp_entry.grid(row=3, column=1)
    

    calculate_button = Button(Bcontainer, text="Calculate now", command = lambda : calc_n_show_BMI(user, heightentry, massentry, calc_resultL, sbp_entry, dbp_entry))
    calculate_button.grid(row=4, column=0) 


    calc_resultL = Label(Bcontainer, text="")
    calc_resultL.grid(row=5, column=0)
 
    
    
    Menu_Button = Button(Bcontainer, text="Back to menu", command=to_Homepage)
    Menu_Button.grid(row=6, column=0, columnspan=2)

    Records_Button = Button(Bcontainer, text="Previous records", command=to_Records_Page)
    Records_Button.grid(row=7, column=0, columnspan=2)

    QuitButton = Button(Bcontainer, text="Quit Program", command=lambda : quit_application(App))
    QuitButton.grid(row=8, column=0, columnspan=2)

        
###########################################page separator###########################################################################

    Rpage = Toplevel(App)

    Rpage.title("Healthie")
    Rpage.geometry(NORMAL)
    
    heading = Label(Rpage, text="Your previous records", font=HEADING)
    heading.pack()

    Rcontainer = Frame(Rpage)
    Rcontainer.pack()

    Rcontainer2 = Frame(Rpage, height=290, width=472)
    Rcontainer2.pack()
    Rcontainer2.pack_propagate(False)

    resultscroll = Scrollbar(Rcontainer2)
    resultscroll.pack(side=RIGHT, fill=Y)

    results = Text(Rcontainer2, yscrollcommand=resultscroll.set)
    filename = format_text(user)
    previous_records = read_records(filename)
    results.insert(INSERT, previous_records)
    results.configure(state="disabled")
    results.pack()

    resultscroll.config(command=results.yview)

    BmiButton = Button(Rcontainer, text="Begin inputting data for BMI", command=to_BMI_Page)
    BmiButton.pack()
    MenuButton = Button(Rcontainer, text="Back to menu", command=to_Homepage)
    MenuButton.pack()
    QuitButton = Button(Rcontainer, text="Quit Program", command=lambda : quit_application(App))
    QuitButton.pack()


    App.mainloop()

def calc_n_show_BMI(user, heightentry, massentry, calc_resultL, sbp_entry, dbp_entry):  #calculates BMI and shows on the application
    h = heightentry.get()
    m = massentry.get()
    SBP = sbp_entry.get()
    DBP = dbp_entry.get()
    line = calc_resultL
    BMI = BMI_Calculator(h, m)
    if BMI <= 18 or BMI >= 25:
        Search_Button(BMI)
    else:
        remove_searchB()            
    show_BMI(BMI, line)
    record_data(user, BMI, SBP, DBP)

def remove_searchB():
    search_B.place_forget()


def Search_Button(BMI): 
    global search_B
    search_B = Button(Bpage, text="Search online for solutions", command=lambda:search_online(BMI))
    search_B.place(x=285, y=112)


def show_BMI(BMI, calc_resultL):    #formats the BMI result with a feedback string
    text = "Your BMI is " + str(BMI) + " " + Defining_Health_Range(BMI)
    textX = text.split(" ")
    for i in range(1, len(textX)):
        if i % 5 == 0:
            textX[i] += "\n"
        else:
            continue
        i += 1
    textY = " ".join(textX) 
    calc_resultL["text"] = textY
   
def record_data(username, BMI, SBP, DBP):   #writes formatted data into text file
    date = datetime.date.today().strftime("%d %b %Y")
    filename = format_text(username)
    write_records(filename, BMI, date, SBP, DBP)
        
def to_Homepage():
    Homepage.lift()

def to_BMI_Page():
    Bpage.lift()

def to_Records_Page():
    Rpage.lift()

def quit_application(App):
    App.update()
    App.deiconify() #reveals the hidden window before destroying it
    App.destroy() 
    rootA.destroy()

def write_BMI_file():   #writes the "BMI.txt" file 
    with open("BMI.txt", "w") as f:
        f.write("""if bodymassindex < 18.5:
Sadly, you're underweight, try changing your diet increase your calorie intake. 
elif bodymassindex < 25:
Yayy! Your body mass is in the normal range! Stay fit and keep it up!
elif bodymassindex < 30:
Hmmm, you're considered overweight, more hard work and try to lower the weight bruh!
elif bodymassindex < 35:
You're Class 1 obese, control your diet!
elif bodymassindex < 40:
You're Class 2 obese, control your diet!
elif bodymassindex >= 40:
You're Class 3 obese, control your diet!        
""")


try:
    check_file(usernamelist)
    Login()   
except:
    create_file(usernamelist)
    write_BMI_file()
    Signup()

