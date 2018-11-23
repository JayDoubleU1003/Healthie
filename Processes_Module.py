import webbrowser

def BMI_Calculator(height, mass):   #calculates BMI
    calculation = (float(mass)/(float(height)*float(height)))
    BMI = float("{:.1f}".format(calculation))
    return BMI

def Defining_Health_Range(BMI):     #gives feedback on BMI condition based on pre-written text file
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
    
def search_online(BMI):     #opens default browser and searches on solution for overweight or underweight solution
    q = ""

    if BMI <= 18.5:
        q = "Underweight solution" 
    elif BMI >= 25:
        q = "Overweight solution"
    

    search = "http://www.google.com/search?hl=en&q=" + q
    webbrowser.open(search)

def read_records(filename): 
    with open(filename, "r") as records:
        text = records.read()
        return text

def write_records(filename, BMI, Date, SBP, DBP):   #formats BMI and blood pressure results and writes into save file

    record_text = "\n| " + str(BMI) + "\t|| \t(" + str(SBP) + ",\t" + str(DBP) + ")\t\t|| " + Date + " |"
    with open(filename, "a") as f:
        f.write(record_text)
