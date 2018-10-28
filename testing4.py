#username = str(input("Please enter new username: "))
#password = str(input("Please enter new password: "))

usernamelist = r"usernamelist.txt"

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

#add_new_user(username, password)

print(check_file(usernamelist))
