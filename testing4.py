from Processes_Module import * 
from Login_New import *
from tkinter import *
import os
import datetime
#import User_Input_Module 

usernamelist = r"usernamelist.txt" #"tempfile.temp"  
HEADING = "TimesNewRoman 14 bold"
SMALL = "150x150+450+250"
NORMAL = "450x400+450+250"

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
    newpassword = pwordE.get()
    existing_accounts = check_file(usernamelist)
    create = True

    for account in existing_accounts:
        if newusername == account["Username"]:
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
        signupagain = Tk() #creates a new window when sign up informations are not provided. 
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
    
        
    
#    except:
#        newusername = nameE.get()
#        create_file(usernamelist)
#        create_file(format_text)
#        add_new_user(nameE.get(), pwordE.get())
#        usersavefile = format_text(newusername)
#        create_save_file(usersavefile)
    

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

def to_application(username):
#    r.destroy()
#    username = nameEL.get()
    Application(username)

def CheckLogin(nameEL, pwordEL):
    global r

    authorized = login(nameEL, pwordEL)
    username = nameEL  

    if authorized:
        to_application(username)
        
#            r = Tk() 
#            r.title("XD")
#            r.geometry(SMALL) 
#            rlbl = Label(r, text = "\n[+] Logged In") 
#            rlbl.pack()
#            continue_Button = Button(r, text = "Continue into app", command = to_application)#, command = Processes_Module.Main_window) 
#            continue_Button.pack()
#            r.mainloop()
        
    else:
        rootA.destroy()
        r = Tk()
        r.title("D:")
        r.geometry(SMALL)
        rlbl = Label(r, text="\n[!] Invalid Login")
        rlbl.pack()
        loginButton = Button(r, text = "Login again", command = Login_again)
        loginButton.pack()
        r.mainloop()

def Login_again():
    r.destroy()
    Login()



def New_Signup():
    rootA.destroy()
    Signup()

def Application(username):
    global Homepage
    global Bpage
    global Rpage
    
    Application = Tk()
    user = username

    Homepage = Toplevel(Application)

    Homepage.title("Healthie")
    Homepage.geometry(NORMAL)

    Hcontainer = Frame(Homepage)
    Hcontainer.pack()

    welcome_text = "Welcome \"" + user + "\""

    heading1 = Label(Homepage, text=welcome_text, font=HEADING)
    heading1.pack()

    BmiButton = Button(Hcontainer, text="Begin inputting data for BMI and blood pressure", command=to_BMI_Page)
    BmiButton.grid()
    RecordsButton = Button(Hcontainer, text="Previous records", command=to_Records_Page)
    RecordsButton.grid()

########################################################################################################################
    
    Bpage = Toplevel(Application) 

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
    dbp_label = Label(Bcontainer, text="Blood pressure(Diastolic")
    dbp_label.grid(row=3, column=0)

    heightentry = Entry(Bcontainer)
    heightentry.grid(row=0, column=1)
    massentry = Entry(Bcontainer)
    massentry.grid(row=1, column=1)
    sbp_entry = Entry(Bcontainer)
    sbp_entry.grid(row=2, column=1)
    dbp_entry = Entry(Bcontainer)
    dbp_entry.grid(row=3, column=1)

    calculate_button = Button(Bcontainer, text="Calculate now", command=calc_n_show_BMI)
    calculate_button.grid(row=4, column=0)

    Menu_Button = Button(Bcontainer, text="Back to menu", command=to_Homepage)
    Menu_Button.grid(row=5, column=0, columnspan=2)

    Save_Button = Button(Bcontainer, text="Save results")#, command=)
    Save_Button.grid(row=4, column=1)

    Records_Button = Button(Bcontainer, text="Previous records", command=to_Records_Page)
    Records_Button.grid(row=6, column=0, columnspan=2)

    result = StringVar()
    resultL = Label(Bcontainer, textvariable = result)
    resultL.grid(row=5, column=0)

########################################################################################################################

    RPage = Toplevel(Application)

    heading = Label(text="Your previous records", font=HEADING)
    heading.pack()

    Rcontainer = Frame(RPage)
    Rcontainer.pack()


    results = Label(Rcontainer, text="")
    filename = format_text(user)
    previous_records = read_records(filename)
    results["text"] = previous_records
#    show_record_B = Button(self, text="Show previous records", command=self.to_display_record)
#    show_record_B.pack()
    BmiButton = Button(Rcontainer, text="Begin inputting data for BMI", command=to_BMI_Page)
    BmiButton.pack()
    MenuButton = Button(Rcontainer, text="Back to menu", command=to_Homepage)
    MenuButton.pack()


    Application.mainloop()

    



def calc_n_show_BMI():
    h = heightentry.get()
    m = massentry.get()
    BMI = BMI_Calculator(h, m)
    text ="Your BMI is " + BMI + "" + Defining_Health_Range(BMI)
    result.set(text)
    date = datetime.date.today().strftime("%d %b %Y")
    username = nameEL.get()
    filename = format_text(username)
    write_records(filename, BMI, date)
        
def to_Homepage():
    Homepage.lift()

def to_BMI_Page():
    Bpage.lift()

def to_Records_Page():
    Rpage.lift()        

    
#        height = heightentry.get()
#        mass = massentry.get()
#        BMI = BMI_Calculator(height, mass)
#        date = datetime.date.today().strftime("%d %b %Y")
#        username = nameEL.get()
#        savefile = format_text(username)
#        write_records(username, BMI, date)

        


    





    



        

#    def read_and_display(self):
#        username = nameEL.get()
#        filename = format_text(username)
#        self.message_var.set(read_records)  





        


        



try:
    check_file(usernamelist)
    Login()   
except:
    create_file(usernamelist)
    Signup()
