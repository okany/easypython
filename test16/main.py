# How do you reverse words in a given sentence without using any library method

class reverser():
    def __init__(self, str1):
        self.str1 = str1
        self.revstr1 = ""

    def reverse(self):

        rvstr1 = ""
        list1 = self.str1.split()

        for item in list1[::-1]:
            rvstr1 = rvstr1 + item.strip() + " "

        return rvstr1


if __name__=="__main__":
    str1 = "Keto looks so good on paper and the results from it are amazing, but why is it such a challenge for me? Am I forever doomed to fail at it? Part of me thought yes, but deep down I knew that if I had the right tools and training wheels, I could make it happen. As I chomped my fourth Oreo I Googled *how to be successful at Keto*."

    rv = reverser(str1)
    print("STRING =", str1)
    print("REVERSE=", rv.reverse())