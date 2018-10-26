import Processes_Module #Imports the module for usage in this file
import User_Input_Module #Imports the module for usage in this file 
import Login_Module



if Login_Module.os.path.isfile(Login_Module.creds):
    Login_Module.Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Login_Module.Signup()


#Processes_Module.Main_window()


