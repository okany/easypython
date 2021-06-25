# check if 2 strings are rotation of each other

class stringrot():
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def isrotate(self):
        if(len(self.str2) != len(self.str1)):
            return False
        if(len(self.str1) == 1):
            return True

        tstr = self.str2
        for i in range(len(self.str2)):
            if(self.str1 == tstr):
                return(True)
            else:
                tstr = tstr[1:] + tstr[0]
        return False

if __name__ == "__main__":
    str1="12312312434t5egfdfvdfopvkfsdocklkxcoksofpwkslck,elrrfgopepoefp;l;sc,lvl;s"
    str2="fpwkslck,elrrfgopepoefp;l;sc,lvl;s12312312434t5egfdfvdfopvkfsdocklkxcokso"

    sr = stringrot(str1,str2)

    print("Is rotate? = ",sr.isrotate())