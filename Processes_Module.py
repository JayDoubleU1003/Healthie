#import Login_New
import webbrowser

def BMI_Calculator(height, mass):
    calculation = float(mass) / ( float(height) * float(height) ) * 10000
    print(calculation)
    BMI = float("{:0.2f}".format(calculation))
    return BMI

def Defining_Health_Range(BMI):
    fileX = open("BMI.txt", "r")
    text = ""

    if BMI < 18.5:
        text = (fileX.readlines()[1])
    elif BMI < 25:
        text = (fileX.readlines()[3])
    elif BMI < 30:
        text = (fileX.readlines()[5])
    elif BMI < 35:
        text = (fileX.readlines()[7])
    elif BMI < 40:
        text = (fileX.readlines()[9])
    elif BMI >= 40:
        text = (fileX.readlines()[11])

    fileX.close()

    return text

def search_online():
    q = input("What do you want?: ")
    search = "http://www.google.com/search?hl=en&q=" + q
    webbrowser.open(search)

def read_records(filename):
    with open(filename, "r") as records:
        text = records.read()
        return text

def write_records(filename, BMI, Date):
    record_text = "\n" + str(BMI) + "\t" + Date
    with open(filename, "a") as f:
        f.write(record_text)
