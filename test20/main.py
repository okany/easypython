# This script checks if a string is palindrome or not

class pstr(str):
    def __init__(self, astr):
        self = astr

    def ispalindrome(self):
        for i in range(int(len(self)/2)):
            if(self[i] != self[len(self)-i-1]):
                return False
        return True

if __name__ == "__main__":

    pstr1 = pstr("123454321")
    print("String {} is Palindrome = {}".format(pstr1, pstr1.ispalindrome()))

    pstr2 = pstr("123456654321")
    print("String {} is Palindrome = {}".format(pstr2, pstr2.ispalindrome()))

    pstr3 = pstr("123454354321")
    print("String {} is Palindrome = {}".format(pstr3, pstr3.ispalindrome()))
