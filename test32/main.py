# This script finds list of all unique triplets in a list of integers satisfying a+b+c=0 in non-descending order

class Solution:

    def __init__(self):
        self.result = None

    # @param A : list of integers
    # @return a list of list of integers
    def order(self, a, b, c):
        if a < b:
            if b < c:
                return ([a, b, c])
            else:
                if a < c:
                    return ([a, c, b])
                else:
                    return ([c, a, b])
        else:
            if a < c:
                return ([b, a, c])
            else:
                if (b < c):
                    return ([b, c, a])
                else:
                    return ([c, b, a])

    def threeSum(self, A):
        mydict = dict()

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                for k in range(j + 1, len(A)):
                    if (A[i] + A[j] + A[k] == 0):
                        item = self.order(A[i], A[j], A[k])
                        key = "{}".format(item)
                        if mydict.get(key) == None:
                           mydict[key] = item
        self.result = mydict
        return mydict


if __name__ == "__main__":
    A = [1, 2, 0, -1, -2, 3, -4, -5, 5, 2, 0]
    sol = Solution()

    md = sol.threeSum(A)
    lst = []
    for item in md.values():
        lst.append(item)

    print("LIST = {}".format(lst))

