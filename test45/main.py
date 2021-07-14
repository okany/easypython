# This script searches for a range (a, b) in a sorted integer array A
# where a and b represent the first and last occurences of integer B

class range_search(list):
    def __init__(self, alist):
        super().__init__(alist)

    def search_int(self, b):
        self.b = b
        self.range = [-1, -1]
        lmin = min = 0
        lmax = max = len(self) - 1

        # stop when you exceed the boundaries which means the int does not exist
        while min <= max:
            pivot = ((max - min) >> 1) + min

            if self[pivot] < self.b:
                min = pivot+1
            elif self[pivot] > self.b:
                max = pivot-1
            else:
                # found a match, just break to continue with the next step
                self.range = [pivot, pivot] # initialize the pivot
                break

        if self[0] != -1: # we must have found the integer
            # print("found the in {} at position {}".format(self.b, pivot))
            lmax = pivot - 1
            lmin = min
            # search the lower bound in the lower list
            while lmin <= lmax:
                lower = ((lmax - lmin) >> 1) + lmin

                # print("lmin={} lmax={} lower={}".format(lmin, lmax, lower))
                if self[lower] < self.b:
                    lmin = lower + 1
                elif self[lower] == self.b:
                    lmax = lower - 1
                    self.range[0] = lower
                else:
                    # this should never happen
                    print("programming error")
                    break

            hmin = pivot + 1
            hmax = max
            # search the upper bound in the higher list
            while hmin <= hmax:
                higher = ((hmax - hmin) >> 1) + hmin

                # print("hmin={} hmax={} higher={}".format(hmin, hmax, higher))
                if self[higher] > self.b:
                    hmax = higher - 1
                elif self[higher] == self.b:
                    hmin = higher + 1
                    self.range[1] = higher
                    break
                else:
                    # this should never happen
                    print("programming error")
                    break

        return(self.range)

if __name__=="__main__":

    res = list()

    array = [1,2,5,7,8,8,8,9,9,9,9,9,10,11,12,15,17,19,21,25]

    ar = range_search(array)
    num = 9
    res = ar.search_int(num)

    print("TEST#1 - range search of {} in array {} resulted as {}".format(num, ar, res))

    array = [1,2,5,7,8,8,8,9,9,9,9,9,10,11,12,15,17,19,21,25]

    ar = range_search(array)
    num = 8
    res = ar.search_int(num)

    print("TEST#2 - range search of {} in array {} resulted as {}".format(num, ar, res))

    array = [1,2,5,7,8,8,8,9,9,9,9,9,10,11,12,15,17,19,21,25]

    ar = range_search(array)
    num = 13
    res = ar.search_int(num)

    print("TEST#3 - range search of {} in array {} resulted as {}".format(num, ar, res))

    array = [1,2,5,7,8,8,8,9,9,9,9,9,10,11,12,15,17,19,21,25]

    ar = range_search(array)
    num = 25
    res = ar.search_int(num)

    print("TEST#4 - range search of {} in array {} resulted as {}".format(num, ar, res))

    array = [1,2,5,7,8,8,8,9,9,9,9,9,10,11,12,15,17,19,21,25]

    ar = range_search(array)
    num = 0
    res = ar.search_int(num)

    print("TEST#5 - range search of {} in array {} resulted as {}".format(num, ar, res))
