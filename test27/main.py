# This script implements a simple vending machine
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

class order():
    def __init__(self, money, item):
        self.money = money
        self.item = item

class item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_str(self):
        astr = "item = (name = " + self.name + " price = "  + str(self.price) + ")"
        return astr

class invitem():
    def __init__(self, item,  count):
        self.item = item
        self.count = count

    def remove(self, num=1):
        self.count = self.count - num

    def add(self, num=1):
        self.count = self.count + num

    def print(self):
        print("{}, count = {}".format(self.item.to_str(), self.count))

class vmachine():
    def __init__(self, list):
        self.dict = dict()
        for each in list:
            self.add(invitem(item(each[0], each[1]), each[2]))

    def add(self, invitem):
        if(self.dict.get(invitem.item.name)):
            self.dict[invitem.item.name].count = self.dict[invitem.item.name].count + invitem.count
        else:
            self.dict[invitem.item.name] = invitem

    def sell(self, order, num=1):
        trans = False
        invitem = self.dict.get(order.item)
        remain = order.money

        if(invitem):
            cost = invitem.item.price*num
            if(cost < order.money):
                trans  = True
                remain = order.money - cost
                invitem.count = invitem.count - num
                return trans, remain
        return trans, remain

    def print(self):
        for each in self.dict.values():
            each.print()

if __name__ == "__main__":

    inv = [["choclate", 10, 25], ["gum", 1, 100], ["coke", 5, 50]]
    vm = vmachine(inv)

    vm.print()

    money = 50

    ord = order(money, "gum")
    trans, money = vm.sell(ord, 5)
    print("transaction = {}, remain = {}".format(trans, money))
    vm.print()

    ord = order(money, "choclate")
    trans, money = vm.sell(ord, 6)
    print("transaction = {}, remain = {}".format(trans, money))
    vm.print()

    ord = order(money, "coke")
    trans, money = vm.sell(ord, 2)
    print("transaction = {}, remain = {}".format(trans, money))
    vm.print()