# This finds the best time to buy and sell a stock once or unlimited times
# to make the maximum profit
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

class best_profit():
    def __init__(self):
        self.maxprofit = self.sellindex = self.sellprice = \
            self.minindex = self.minprice = 0

    def print(self):
        print("MAXPROFIT = {}".format(self.maxprofit))
        print("Buy for {} on index {}".format(self.minprice, self.minindex))
        print("Sell for {} on index {}".format(self.sellprice, self.sellindex))

class stock_prices(list):

    def __init__(self, list):
        super().__init__(list)

    def max_profit_once(self):

        bp = best_profit()
        bp.minprice = self[0]
        profit = 0

        # iterate over price list to determine th best profit
        for index in range(len(self)):
            # keep track off the min price
            if self[index] < bp.minprice:
                bp.minprice = self[index]
                bp.minindex = index

            # check the profit if we sell now
            profit = self[index] - bp.minprice

            # replace the maxprofit if profit is more than maxprofit
            if(profit > bp.maxprofit):
                bp.maxprofit = profit
                bp.sellprice = self[index]
                bp.sellindex = index

        return bp

    def max_profit_unlimited(self):

        bplist = list()
        bplist.append(best_profit())
        total_profit = sellno = 0
        bplist[sellno].minprice = self[0]

        # iterate over price list to determine th best profit
        for index in range(1, len(self)):

            print("index= {} {} {} {}".format(index, bplist[sellno].minindex,
                                              self[index], self[index-1]))
            # price decrease indicates a sell point
            if self[index] < self[index-1] and bplist[sellno].maxprofit > 0:
                print("selling ... index = {}".format(index))
                total_profit += bplist[sellno].maxprofit
                sellno += 1
                bplist.append(best_profit())
                bplist[sellno].minindex = index
                bplist[sellno].minprice = self[index]

            # keep track off the min price
            if self[index] < bplist[sellno].minprice:
                bplist[sellno].minprice = self[index]
                bplist[sellno].minindex = index

            # check the profit if we sell now
            profit = self[index] - bplist[sellno].minprice

            # replace the maxprofit if profit is more than maxprofit
            if(profit > bplist[sellno].maxprofit):
                bplist[sellno].maxprofit = profit
                bplist[sellno].sellprice = self[index]
                bplist[sellno].sellindex = index

        if(bplist[sellno].maxprofit > 0):
            total_profit += bplist[sellno].maxprofit

        return total_profit, bplist

if __name__=="__main__":

    sprices = (5, 3, 2, 10, 12, 15, 17, 11, 6, 8 , 10, 20, 23, 17, 15, 16, 18, 20, 26, 50, 13, 24, 45, 49)
    sp = stock_prices(list(sprices))

    mpo = sp.max_profit_once()
    print ("MAX PROFIT ONCE")
    mpo.print()

    maxprofit, mpu = sp.max_profit_unlimited()

    print("\n\nMAX PROFIT UNLIMITED")
    print("Total Profit = {}".format(maxprofit))
    for i in range(len(mpu)):
        print("SELL #{}".format(i))
        mpu[i].print()
