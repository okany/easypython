# This script finds a, b, c, d values such that A[a]+A[b] = A[c] + A[d] where
# a < b and c < d and a < c and b != d and b != c

class intarray():
    def __init__(self, alist):
        self.alist = alist
        self.adict = dict()
        self.soln = None

    def check_solution(self, soln):
        # print("self.soln = {} soln = {}".format(self.soln, soln))
        if self.soln == None:
            self.soln = soln
        else:
            if self.soln[0] > soln[0] or \
                ((self.soln[0] == soln[0]) and (self.soln[1] > soln[1])) or \
                ((self.soln[0] == soln[0]) and (self.soln[1] == soln[1]) and (self.soln[2] > soln[2])) or \
                ((self.soln[0] == soln[0]) and (self.soln[1] == soln[1]) and \
                 (self.soln[2] == soln[2]) and (self.soln[3] > soln[3])):
                self.soln = soln
                return

    def find_equals(self):
        retval = list()
        self.adict = dict() # reset the sum dictionary

        for aind in range(len(self.alist)):
            for bind in range(aind+1, len(self.alist)):
                sum = self.alist[aind] + self.alist[bind]
                # print("checking {} {}".format(aind, bind))
                dval = self.adict.get(sum)
                if (dval):
                    # print("found a possible solution {} {} {} {}".format(dval[0], dval[1], aind, bind))
                    if (dval[0] < aind) and dval[1] != aind and dval[1] != bind:
                        soln = list(dval)
                        # create the list [A, B, C, D]
                        soln.append(aind)
                        soln.append(bind)
                        self.check_solution(soln)
                else:
                    # print("adding {} {} with values {} {} to the dict".
                    #        format(aind, bind, self.alist[aind], self.alist[bind]))
                    self.adict[sum] = [aind, bind]
        return self.soln

if __name__ == '__main__':

    alist = [2, 1, 3, 5, 6, 4, 10, 8, 7]

    ia = intarray(alist)

    print("A+B = C+D list of {} is {} ".format(alist, ia.find_equals()))