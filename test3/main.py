# This script manipulates a number string by
# adding a "*" between two consecutive even numbers and "-" between two consecutive odd numbers

class strmanup():
    def __init__(self, astr):
        self.astr = astr
        self.offset = 0

    def isEven(self, i):
        return((int(self.astr[i]) % 2) == 0)

    def isOdd(self, i):
        return((int(self.astr[i]) % 2) != 0)

    def manupstr(self, offset):
        newstr = ""
        if(len(self.astr)<offset):
            return self.astr

        for i in range(len(self.astr)-offset+1):
            newstr = newstr + self.astr[i]
            if (self.isEven(i) and self.isEven(i+1)):
                newstr = newstr + "*"
            elif (self.isOdd(i) and self.isOdd(i+1)):
                newstr = newstr + "-"
        return newstr

if __name__ == '__main__':
    astr = "1235353565675675567889098"
    offset = 2

    strobj = strmanup(astr)

    print("NEWSTR=", strobj.manupstr(2))

