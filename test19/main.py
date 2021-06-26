# This script finds all combinations of a string

class strcomb(str):
    def __init__(self, astr):
        self.comb = []
        self = astr

    def findallcombs(self):
        self.findcombs(self)
        return(self.comb)

    def findcombs(self, astr):
        if astr == "": pass
        elif len(astr) == 1:
            self.comb.append(astr)
        else:
            bstr = strcomb(astr[1:])
            alcomb = bstr.findallcombs()
            for item in alcomb:
                for i in range(len(item)+1):
                    self.comb.append(item[:i]+astr[0]+item[i:])

# using a class makes the code complicated
# this is a utility function which does not use a class
def findcombs2(astr):
    if astr == []: pass #return empty list if the string is empty
    elif len(astr) == 1: #return a list with a single char string
        return [astr]
    else:
        # save hte first char and look for string combinations in the rest of the string
        alcomb = findcombs2(astr[1:])
        newcomb = []
        for item in alcomb:
            # include item + astr[0] as well
            for i in range(len(item)+1):
                newcomb.append(item[:i]+astr[0]+item[i:])
        return newcomb

if __name__ == "__main__":
    str1 = "abcde"
    st1 = strcomb(str1)

    alcombs = st1.findallcombs()
    print("Class version:")
    print("There are {} combinations: {}".format(len(alcombs), alcombs))

    alcombs2 = findcombs2(str1)
    print("Utility function version:")
    print("There are {} combinations: {}".format(len(alcombs2), alcombs2))
