# How can a given string be reversed using recursion?


def reversestr(astr):
    if(astr == "" or len(astr) == 1):
        return astr
    else:
        return(reversestr(astr[1:len(astr)]) +  astr[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    astr = "jwekjrkwjekrbmsndmfnsmdf"
    print("STR1= ", reversestr(astr))

    bstr = ""
    print("STR2= ", reversestr(bstr))

    cstr = "2"
    print("STR3= ", reversestr(cstr))

