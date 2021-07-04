# This script reads a text file and creates another text file with the
# reversed file content (each line in reverse order and words in each line
# are also reversed)
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

if __name__=="__main__":
    try:
        fname = input("Input file name > ")
        outname = fname.split(".")[0] + ".out"

        infile = open(fname)
        outfile = open(outname, "w")

        fcontent = []
        ocontent = []
        line = infile.readline()
        while (line):
            fcontent.append(line)
            line = infile.readline()

        for each in fcontent[::-1]:
            words = each.split()
            reverse = ""
            for word in words[::-1]:
                reverse = reverse + word + " "
            reverse = reverse + "\n"
            ocontent.append(reverse)

        outfile.writelines(ocontent)

    except IOError as ioerr:
        print("received an IOError {}".format(ioerr))
    except:
        print("received a generic error {}".format(sys.exc_info()))
