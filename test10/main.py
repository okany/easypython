# How do you print the first non-repeated character from a string?

class firstnrep(str):
    def __init__(self, astr):
        self.set = set()
        self.first = ""
        self = astr

    def firstnon(self):
        self.first = ""
        for char in self[::-1]:
            if char not in self.set:
                self.set.add(char)
                self.first = char

        return self.first

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    astr = "sdklklrtiojkeksrdll"

    fnrs = firstnrep(astr)
    print("First Non-repeated char= {}".format(fnrs.firstnon()))