# this script determines if two strings are anagram or not

def isanogram(str1, str2):
    for char in str1:
        ind = str2.find(char)
        if ind >= 0:
            str2 = str2[0:ind] + str2[ind+1:]
        else:
            return (False)

    if str2 == "":
        return(True)

    return(False)

if __name__ == '__main__':
    str1 = "abcdefghau6uucdek"
    str2 = "abufdeccgha6dekuu"

    print("IS ANOGRAM=", isanogram(str1, str2))

