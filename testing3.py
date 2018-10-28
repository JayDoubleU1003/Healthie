username = str(input("Please enter new username: "))
password = str(input("Please enter new password: "))

usersavefile = r"accounts\\" + username + ".txt" 
usernamelist = r"usernamelist.txt"

def create_file(file_name):
    with open(file_name, "w") as f:
        f.write("[]")

def check_file(file_name):
    with open(file_name, "r") as pull_file:
        f = eval(pull_file.read())
    return f

def add_new_user(newusername, newpassword):
    new_account = {"Username": newusername, "Password": newpassword}
    existing_accounts = check_file(usernamelist) 

    existing_accounts.append(new_account)    

    f = open(usernamelist, "w")
    f.write("{}".format(existing_accounts))

#def check_username(newusername):
#    existing_accounts = check_file(usernamelist)


try:
    check_file(usernamelist)
    add_new_user(username, password)
except:
    create_file(usernamelist)
    add_new_user(username, password)
