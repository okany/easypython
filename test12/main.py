# check if a string has all digits

class digitstr(str):

    def __init__(self, astr):
        self = astr

    def alldigits(self):
        if self == "": return False
        else: return(self.checkdig(self))

    def checkdig(self, astr):
        if(astr == ""):
            return True
        elif(astr[0].isdigit()):
            return self.checkdig(astr[1:])
        else:
            return False

if __name__ == '__main__':

    astr = digitstr("23423423y5")
    print("alldigit? = ", astr.alldigits())
