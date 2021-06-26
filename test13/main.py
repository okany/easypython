# This script reverses words in a paragraph

def reverse(alist):
    blist = []
    for item in alist:
        blist.insert(0,item)
    return blist

def reverse2(alist):
    blist = []
    for item in alist[::-1]:
        blist.append(item)
    return blist

if __name__ == "__main__":
    astr = "In this study we used domain engineering as a method for gaining deeper formal understanding of a class of algorithms. Specifically, we analyzed 6 stemming algorithms from 4 different sub-domains of the conflation algorithms domain and developed formal domain models and generators based on these models. The application generator produces source code for not only affix removal but also successor variety, table lookup, and n-gram stemmers. The performance of the generated stemmers was compared with the stemmers developed manually in terms of stem similarity, source, and executable sizes, and development and execution times. Five of the stemmers generated by the application generator produced more than 99.9% identical stems with the manually developed stemmers. Some of the generated stemmers were as efficient as their manual equivalents and some were not."

    alist = list(astr.split())

    print("reverse of {} is {}".format(alist, reverse(alist)))
    print("reverse2 of {} is {}".format(alist, reverse2(alist)))