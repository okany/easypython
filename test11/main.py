# How can a given string be reversed using recursion?

class rstr(str):
    def __init__(self, astr):
        self = astr

    def reverse(self):
        return(self.reversestr(self))

    def reversestr(self, astr):
        if(astr == "" or len(astr) == 1):
            return astr
        else:
            return(self.reversestr(astr[1:]) +  astr[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    astr = rstr("jwekjrkwjekrbmsndmfnsmdf")
    print("TEST#1 - reverse of string {} is {} ".format(astr, astr.reverse()))

    bstr = rstr("")
    print("TEST#2 - reverse of string {} is {} ".format(bstr, bstr.reverse()))

    cstr = rstr("2")
    print("TEST#3 - reverse of string {} is {} ".format(cstr, cstr.reverse()))

