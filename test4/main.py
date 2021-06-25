# mingle two strings after crerating chunks in size n
# e.g. ABCDEFG and 1234567890 with 2 char chunks -> AB12CD34EF56G7890

class merger():
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    lista = listb = []

    def merge(self, offset):
        flist = list()

        if len(self.list1) < len(self.list2):
            lista = self.list1
            listb = self.list2
        else:
            listb = self.list1
            lista = self.list2

        times = int(len(lista)/offset)
        for i in range(times):
            flist = flist + lista[i*offset:i*offset+offset]
            flist = flist + listb[i*offset:i*offset+offset]
        flist = flist + lista[times*offset:len(lista)]
        flist = flist + listb[times*offset:len(listb)]

        return(flist)

if __name__ == '__main__':

    # TEST#1
    tlist1a = ["2","3","4","2","3","5","2","4","3","5","6","4","5"]
    tlist1b = ["a","s","d","a","s","d","a","s","f","d","s","g","g","d","f","g","d","f","f","g","h","j","f","g","h","j","g","h","j"]

    m1 = merger(tlist1a, tlist1b)
    num1 = 2
    print("TEST1 - {} char merged list = {}".format(num1, m1.merge(num1)))

    # TEST#2
    tlist2a = ["1","2","3","2","3","4","2","4","5","3","6","4","5","7","5","6","7","5","8","6","7","9","7","8","0","8","9","0"]
    tlist2b = ["x","c","v","x","c","v","c","v","b","n","f","g","h","y","r","t","y","r","t","y"]

    m2 = merger(tlist2a, tlist2b)
    num2 = 3
    print("TEST2 - {} char merged list = {}".format(num2, m2.merge(num2)))

    # TEST#3
    tlist3a = ["5","6","7","8","9"]
    tlist3b = ["q","w","e","s","k"]

    m3 = merger(tlist3a, tlist3b)
    num3 = 4
    print("TEST3 - {} char merged list = {}".format(num3, m3.merge(num3)))

