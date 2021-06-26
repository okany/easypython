# This script removes duplicate entries in a list

class uniquelist(list):
    def __init__(self, alist):
        super().__init__(alist)
        self.set = set()
        self.rlist = []

    def dedup(self):
        self.rlist = []
        for i in range(len(self)):
            item = self[i]
            if item not in self.set:
                self.set.add(item)
                self.rlist.append(item)
        return (self.rlist)

    def dedup2(self):
        self.rlist = self
        i = len(self.rlist) - 1
        while i > 0:
            item = self.rlist[i]
            if(item not in self.set):
                self.set.add(item)
            else:
                self.rlist.pop(i)
            i = i - 1
        return(self.rlist)

if __name__ == "__main__":
    str1 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."
    alist1 = str1.split()

    ul1 = uniquelist(alist1)
    print(ul1.dedup())

    str2 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."
    alist2 = str2.split()

    ul2 = uniquelist(alist2)
    print(ul2.dedup2())

