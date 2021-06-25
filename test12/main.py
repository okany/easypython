# How do you check if a string has all digits


def alldigits(astr):
    if astr == []: return False
    else: return(checkdig(astr))

def checkdig(astr):
    if(astr == ""):
        return True
    elif(astr[0].isdigit()):
        return checkdig(astr[1:])
    else:
        return False

if __name__ == '__main__':
    astr = "23423423y5"

    ad = alldigits(astr)
    print("alldigit? = ", ad)
