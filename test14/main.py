# This script removes duplicate entries in a list

class uniquelist():
    def __init__(self, alist):
        self.alist = alist
        self.set = set()

    def dedup(self):
        blist = []
        for i in range(len(self.alist)):
            item = self.alist[i]
            if item not in self.set:
                self.set.add(item)
                blist.append(item)
        self.alist = blist
        return (self.alist)

    def dedup2(self):
        blist = []
        i = len(self.alist) - 1
        while i > 0:
            item = self.alist[i]
            if(item not in self.set):
                self.set.add(item)
            else:
                self.alist.pop(i)
            i = i - 1
        return(self.alist)

if __name__ == "__main__":
    str1 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."
    alist1 = str1.split()

    ul1 = uniquelist(alist1)
    print(ul1.dedup())

    str2 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."
    alist2 = str2.split()

    ul2 = uniquelist(alist2)
    print(ul2.dedup2())

