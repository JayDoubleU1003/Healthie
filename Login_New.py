import os
import Processes_Module
 
usernamelist = r"usernamelist.txt" #"tempfile.temp"  


 
def create_file(file_name):
    with open(file_name, "w") as f:
        f.write("[]")


def create_save_file(file_name):
        try :
                check_file(file_name)
                with open(file_name, "w") as f:
                        f.write("")

        except:
                try:
                        os.mkdir("accounts")
                        with open(file_name, "w") as f:
                                f.write("") 
                except:
                        with open(file_name, "w") as f:
                                f.write("")




def check_file(file_name):
    with open(file_name, "r") as pull_file:
        f = eval(pull_file.read())
    return f

def add_new_user(newusername, newpassword):
    new_account = {"Username": newusername, "Password": newpassword}
    existing_accounts = check_file(usernamelist)

    existing_accounts.append(new_account)    

    with open(usernamelist, "w") as f:
        f.write("{}".format(existing_accounts))

def format_text(username):
        f = r"accounts\\" + username + ".txt"
        return f

def login(entry_username, entry_password):
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
 
#def DelUser():
#    os.remove(creds) 
#    rootA.destroy() 
#    Signup() 
 
#if os.path.isfile(creds):
#    Login()
#else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
#    Signup()"
