#import Login_New
import webbrowser

def BMI_Calculator (height, mass):
    global BMI
    BMI = float(mass)/float(height)*float(height)
    print("{:.1f}".format(BMI))
    return BMI

def Defining_Health_Range (BMI):
    fileX = open("BMI.txt", "r")
    
    if BMI < 18.5:
        print(fileX.readlines()[1])
    elif BMI < 25:
        print(fileX.readlines()[3])
    elif BMI < 30:
        print(fileX.readlines()[5])
    elif BMI < 35:
        print(fileX.readlines()[7])
    elif BMI < 40:
        print(fileX.readlines()[9])
    elif BMI >= 40:
        print(fileX.readlines()[11])
    
    fileX.close
    
def search_online():
    q = input("What do you want?: ")
    search = "http://www.google.com/search?hl=en&q=" + q
    webbrowser.open(search)

def read_records(filename):
    with open(filename, "r") as records:
        return records.read()

def write_records(username, BMI, Date):
    record_text = BMI + "\t" + Date
