#import Login_New
import webbrowser

def BMI_Calculator(height, mass):
    calculation = (float(mass)/(float(height)*float(height)))
    BMI = float("{:.1f}".format(calculation))
    return BMI

def Defining_Health_Range(BMI):
    fileX = open("BMI.txt", "r")
    
    text = ""

    if BMI < 18.5:
        text = (fileX.readlines()[1])
        return text
    elif BMI < 25:
        text = (fileX.readlines()[3])
        return text
    elif BMI < 30:
        text = (fileX.readlines()[5])
        return text
    elif BMI < 35:
        text = (fileX.readlines()[7])
        return text
    elif BMI < 40:
        text = (fileX.readlines()[9])
        return text
    elif BMI >= 40:
        text = (fileX.readlines()[11])
        return text
    
    fileX.close
    
def search_online():
    q = input("What do you want?: ")
    search = "http://www.google.com/search?hl=en&q=" + q
    webbrowser.open(search)

def read_records(filename):
    with open(filename, "r") as records:
        text = records.read()
        return text

def write_records(filename, BMI, Date, SBP, DBP):
    record_text = "\n|\t" + str(BMI) + "\t\t||\t\t(" + str(SBP) + ",\t" + str(DBP) + ")\t||\t" + Date + "\t|"
    with open(filename, "a") as f:
        f.write(record_text)
