import os
 
usernamelist = r"usernamelist.txt"   


 
def create_file(file_name):    
    with open(file_name, "w") as f:
        f.write("[]")


def create_save_file(file_name):        #creates folder for user save files
        first_line = "| BMI\t||   Blood Pressure(SBP, DBP)   ||\tDate\t\t\t\t    |"

        try :
                check_file(file_name)
                with open(file_name, "w") as f:
                        f.write("")

        except:
                try:
                        os.mkdir("accounts")
                        with open(file_name, "w") as f: 
                                f.write(first_line) 
                except:
                        with open(file_name, "w") as f:
                                f.write(first_line)



def check_file(file_name): #checks whether file is available or not
    with open(file_name, "r") as pull_file:
        f = eval(pull_file.read())
    return f

def add_new_user(newusername, newpassword):     #adds new user details into record
    new_account = {"Username": newusername, "Password": newpassword}
    existing_accounts = check_file(usernamelist)

    existing_accounts.append(new_account)    

    with open(usernamelist, "w") as f:
        f.write("{}".format(existing_accounts))

def format_text(username):      #formats username into save file name
        f = r"accounts\\" + username + ".txt"
        return f

def login(entry_username, entry_password):      #checks login information 
    authorized = False
    existing_accounts = check_file(usernamelist)

    username = entry_username
    password = entry_password

    for account in existing_accounts:
        if username == account["Username"] and password == account["Password"]:
            authorized = True
            break
        else:
            continue

    return authorized
