# Find duplicate characters in a string

class stringdups():
    def __init__(self, astr):
        self.str = astr
        self.strdict = dict()
        self.strdups = []

    def finddups(self):
        for char in self.str:
            if self.strdict.get(char) == None:
                self.strdict[char] = 1
            else:
                self.strdict[char] = self.strdict[char] + 1
                if self.strdict[char] == 2:
                    self.strdups.append(char)

        return(self.strdups)


if __name__ == "__main__":
    str1 = "2293049o055776276122-059068607867874860-60940487827628a78478876969708t0-78-08-50498398201u9182a989o85095079089-"

    sd1 = stringdups(str1)
    print("DUPS1 = {}".format(sd1.finddups()))

    str2 = ""

    sd2 = stringdups(str2)
    print("DUPS2 = {}".format(sd2.finddups()))
