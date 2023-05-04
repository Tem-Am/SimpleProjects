from pickle import NEWFALSE
from phoneclass import Phone

def funciton1(deff):
    translation = ""
    for anyletter in deff:
        if anyletter.lower() in "aeiou":
            if anyletter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + anyletter
    return translation

##myFile = open("newfile12.txt", "w")

##myFile.write("\nwooow")
##myFile.close()
phone1 = Phone("TemPhone", True, "Iphone13", 1000)
print(phone1.price)