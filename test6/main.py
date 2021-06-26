# This script demonstrates trying and catching exceptions while getting an a positive integer as an input
# and printing its square

class square(int):
    def __init__(self, num):
        self = num

    def getnum(self):
        return self

    def getsqr(self):
        return (self * self)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:
        numstr = input("Enter a number: ")
        num = int(numstr)
        if num < 0: raise ValueError
    except NameError:
        print("Name Error")
    except ValueError:
        print("Value Error")
    except IOError:
        print("I/O Error")
    except:
        print("not a valid entry")
    else:
        numobj = square(num)
        print("Square of {0} is {1}".format(numobj.getnum(), numobj.getsqr()))
