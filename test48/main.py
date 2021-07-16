# This script finds all unique permutations of a list of numbers

def find_perms(perm):
    aset = set(range(len(perm)))
    # print("set is {}".format(aset))
    perm.find_perms(aset, [])
    for each in perm.perms.values():
        perm.permlist.append(each)

class permutations(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.perms = dict()
        self.sort()
        self.set = set(range(len(self)))
        self.permlist = []

    def add_soln(self, alist):
        astr = ""
        for each in alist:
            astr = str(each) + "-" + astr

        # print("adding solution {}".format(astr))
        perm = self.perms.get(astr)
        if perm == None:
            self.perms[astr] = alist

    def find_perms(self, aset, alist):
        # print("fiding perms of {} alist {}".format(aset, alist))
        # stopping case all elements are used
        if aset == set():
            self.add_soln(alist)
        else:
            for i in aset:
                tset = aset.copy()
                # remove the current element
                tset.remove(i)
                tlist = alist.copy()
                tlist.append(self[i])
                self.find_perms(tset, tlist)

if __name__ == "__main__":

    alist = [1, 1, 2]
    p = permutations(alist)
    find_perms(p)
    print("TEST#1 - {} unique permutations of {} are {}".format(len(p.permlist), alist, p.permlist))

    alist = [1, 1, 2, 2]
    p = permutations(alist)
    find_perms(p)
    print("TEST#2 - {} unique permutations of {} are {}".format(len(p.permlist), alist, p.permlist))

    alist = [1, 1, 2, 3, 4 , 4]
    p = permutations(alist)
    find_perms(p)
    print("TEST#3 - {} unique permutations of {} are {}".format(len(p.permlist), alist, p.permlist))
