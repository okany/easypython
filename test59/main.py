# This script converts a JSON string into prettyJSON format
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright (c) 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
class prettyJSON(str):
    def __init__(self, astr):
        super().__init__()
        self.json = ""
        self.popen = "{"
        self.pclose = "}"
        self.bopen = "["
        self.bclose = "]"
        self.comma = ","
        self.indent = 0
        self.tab = "    "
        self = astr

    def print_indented(self, astr):
        if astr == "":
            return
        for each in range(self.indent):
            print("{}".format(self.tab), end = '')
        print("{}".format(astr), end ='')

    def parse_paren(self, astr, paren):
        po = astr.find(paren)
        bstr = astr[:po]
        cstr = astr[po:]
        # print("bstr={}, cstr={}".format(bstr, cstr))
        self.parse(bstr)
        print("")
        self.parse(cstr)

    def parse(self, astr, comma=False):
        #print("==={}====".format(astr))
        if astr == "":
            return
        elif astr[0] == self.popen or astr[0] == self.bopen:
            bstr = astr[1:]
            self.print_indented("{}\n".format(astr[0]))
            self.indent += 1
            self.parse(bstr)
        elif astr[0] == self.pclose or astr[0] == self.bclose:
            bstr = astr[1:]
            self.indent -= 1
            if bstr != "" and bstr[0]==",":
                self.print_indented("{},\n".format(astr[0]))
                bstr = bstr[1:]
            else:
                self.print_indented("{}\n".format(astr[0]))
            self.parse(bstr)
        elif astr.find(self.popen) != -1:
            self.parse_paren(astr, self.popen)
        elif astr.find(self.pclose) != -1:
            self.parse_paren(astr, self.pclose)
        elif astr.find(self.bopen) != -1:
            self.parse_paren(astr, self.bopen)
        elif astr.find(self.bclose) != -1:
            self.parse_paren(astr, self.bclose)
        elif astr.find(self.comma) == -1:
            self.print_indented(astr)
        else:
            alist = astr.split(self.comma)
            for each in alist[:-1]:
                self.parse(each, True)
            if(len(alist)>0):
                self.parse(alist[-1])
        if comma == True:
            print(",")

    def pretty_print_JSON(self):
        self.parse(self)

    def parse_chars(self):
        self.indent = 0
        istart = 0
        i = 0
        while i < len(self):
            if self[i] == self.bopen or self[i] == self.popen:
                if istart < i:
                    self.print_indented(self[istart:i] + "\n")
                self.print_indented(self[i]+"\n")
                self.indent += 1
                istart = i + 1
            elif self[i] == self.bclose or self[i] == self.pclose:
                if istart < i:
                    self.print_indented(self[istart:i] + "\n")
                self.indent -= 1
                if i+1 < len(self) and self[i+1] == self.comma:
                    self.print_indented(self[i:i+2] + "\n")
                    istart = i + 2
                    i += 1
                else:
                    self.print_indented(self[i]+"\n")
                    istart = i + 1
            elif self[i] == self.comma:
                self.print_indented(self[istart:i+1] + "\n")
                istart = i + 1
            i += 1

    def pretty_print_JSON2(self):
        self.parse_chars()

if __name__=="__main__":

    print("TEST#1")
    astr = "{A:'1',B:'2',C:{D:{E:'3',F:{G:{H:'4'},I:{J:'5'},K:{L:'6'}},M:'7',N:'8'},O:'9'}}"

    pj = prettyJSON(astr)
    pj.pretty_print_JSON()
    pj.pretty_print_JSON2()

    print("TEST#2")
    astr = "{'apple','orange','melon':['banana':['cherry','peach',0,1.5,2],'lemon'],'blueberry'}"

    pj = prettyJSON(astr)
    pj.pretty_print_JSON()
    pj.pretty_print_JSON2()

    print("TEST#3")
    astr = "{4,'ashburn',['sterling':['reston','arlington',9,5.3,2.8],'falls church'],'annandale'}"

    pj = prettyJSON(astr)
    pj.pretty_print_JSON()
    pj.pretty_print_JSON2()
