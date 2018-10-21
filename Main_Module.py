import Processes_Module  #Imports the module for usage in this file
import User_Input_Module #Imports the module for usage in this file 

print("Health Monitor") 
x = input("Press 'Enter' to start recording body mass index, enter 'x' to end program: ")

if x == "": 
    height = float(input("Enter your height in meters: "))
    mass = float(input("Enter your mass in Kg: "))
    Processes_Module.BMI_Calculator(height, mass)
    Processes_Module.Defining_Health_Range(Processes_Module.BMI) #calls Defining_Health_Range function from Processes_Module

elif x.lower() == "x": 
    print("Alright. This program ends here")


