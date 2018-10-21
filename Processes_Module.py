


def BMI_Calculator (height, mass):
    global BMI
    BMI = mass/(height*height)
    print("{:.1f}".format(BMI))
    return BMI


def Defining_Health_Range (BMI):
    fileX = open(r"C:\Users\Jw Lim\Python\Swinburne\BMI.txt", "r")
    
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
    
