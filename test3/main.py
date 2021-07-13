# This script finds the best time to buy and sell a stock once or unlimited times
# or fix number of time to make the maximum profit
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
    def __init__(self, sp):
        self.sp = sp
        self.sellindex = self.buyindex = 0

    def profit(self):
        # if seelindex does not have the default value
        if self.sellindex == 0:
            return 0
        else:
            return self.sp[self.sellindex] - self.sp[self.buyindex]
    def setbuyindex(self, buyindex):
        self.buyindex = buyindex

    def setsellindex(self, sellindex):
        self.sellindex = sellindex

    def sellprice(self):
        return self.sp[self.sellindex]

    def buyprice(self):
        return self.sp[self.buyindex]

    def print(self):
        print("MAXPROFIT = {}".format(sp[self.sellindex] - sp[self.buyindex]))
        print("Buy for {} on index {}".format(sp[self.buyindex], self.buyindex))
        print("Sell for {} on index {}".format(sp[self.sellindex], self.sellindex))

class stock_prices(list):

    def __init__(self, alist):
        super().__init__(alist)
        self.bplist = list()
        self.actlist = list()
        self.costlist = list()

    def max_profit_once(self):

        bp = best_profit(self)
        bp.buyindex = 0
        profit = 0

        # iterate over price list to determine th best profit
        for index in range(len(self)):
            # keep track off the min price
            if self[index] < self[bp.buyindex]:
                bp.setbuyindex(index)

            # check the profit if we sell now
            profit = self[index] - self[bp.buyindex]

            # replace the maxprofit if profit is more than maxprofit
            if(profit > self[bp.sellindex] - self[bp.buyindex]):
                bp.sellindex = index

        return bp

    # this function determines the bet buy and sell times when unlimited number
    # of trades are allowed
    def max_profit_unlimited(self):

        self.bplist = list()
        self.bplist.append(best_profit(self))
        total_profit = sellno = 0

        # iterate over price list to determine the best profit
        for index in range(1, len(self)):

            # print("sellno = {} index= {} {} {} {}".
            #      format(sellno, index, self.bplist[sellno].buyindex,
            #             self[index], self[index-1]))
            # print(self.bplist[sellno].profit())
            # price decrease indicates a sell point
            if self[index] < self[index-1] and self.bplist[sellno].profit() > 0:

                # print("selling ... index = {}".format(index-1))
                # update merge cost list
                # self.update_merge_cost(sellno)
                total_profit += self.bplist[sellno].profit()
                sellno += 1
                self.bplist.append(best_profit(self))
                self.bplist[sellno].setbuyindex(index)

            # keep track off the min price
            if self[index] < self[self.bplist[sellno].buyindex]:
                self.bplist[sellno].setbuyindex(index)

            # check the profit if we sell now
            profit = self[index] - self.bplist[sellno].buyprice()

            # replace the maxprofit if profit is more than maxprofit
            if(profit > self.bplist[sellno].profit()):
                self.bplist[sellno].sellindex = index

        if(self.bplist[sellno].profit() > 0):
            print("selling ... index = {}".format(index))
            # update merge cost list
            # self.update_merge_cost(sellno)
            total_profit += self.bplist[sellno].profit()
        else:
            self.bplist.pop(sellno)

        return total_profit, self.bplist

    # this is an alternative implementation of unlimited trades
    # this function creates the all buy sell points that will be used
    # to determine the maximum profit when at most X number of trades is allowed
    def max_profit_all(self):

        self.actlist = list()
        total_profit = actindex = 0
        downtrend = True
        self.actlist.append(0)

        # iterate over price list to determine the best profit
        for index in range(1, len(self)):

            if downtrend:
                if self[index] < self[index-1]:
                    self.actlist[actindex] = index
                elif self[index] > self[index-1]:
                    # local min found - buy point
                    self.actlist.append(index)
                    # self.tradesort(actindex-1)
                    actindex += 1
                    downtrend = False
            else:
                if self[index] > self[index -1]:
                    self.actlist[actindex] = index
                elif self[index] < self[index-1]:
                    # local max found - sell point
                    self.actlist.append(index)
                    # cash it - add profit to the total
                    total_profit += self[self.actlist[actindex]] - self[self.actlist[actindex-1]]
                    actindex += 1
                    downtrend = True

        if downtrend:
            # remove the last activity node - nothing to sell
            self.actlist.pop(actindex)
            actindex -= 1

        total_profit = self.set_bplist_from_actlist()

        return total_profit, self.actlist

    def trade_cost(self, index):
        # cost of removing a trade = absolute value of price of this trade - price of next trade
        return(abs(self[self.actlist[index]] - self[self.actlist[index+1]]))

    def set_bplist_from_actlist(self):
        total_profit = 0
        self.bplist = list()
        for i in range(len(self.actlist)-1):
            if self[self.actlist[i+1]] > self[self.actlist[i]]:
                bp = best_profit(self)
                bp.setbuyindex(self.actlist[i])
                bp.setsellindex(self.actlist[i+1])
                total_profit += bp.profit()
                self.bplist.append(bp)

        return total_profit

    def keep_best_trades(self, n):
        self.legs = 2 * n

        while len(self.actlist) > self.legs:
            minindex = 0
            for i in range(len(self.actlist)-1):
                if(self.trade_cost(i) <  self.trade_cost(minindex)):
                    minindex = i

            # remove two activities to eliminate the least beneficial trade
            self.actlist.pop(minindex)
            self.actlist.pop(minindex)

        total_profit = self.set_bplist_from_actlist()

        print("ACTIVITY LIST= {}".format(self.actlist))
        return total_profit, self.actlist

    def max_profit_limited(self, numoftrades):
        total_profit = 0
        bplist = list()
        actlist = list()

        total_profit, actlist = self.max_profit_all()

        total_profit, actlist = self.keep_best_trades(numoftrades)

        return (total_profit, actlist)
    def print_bplist(self):
        for i in range(len(self.bplist)):
            print("SELL #{}".format(i))
            self.bplist[i].print()


if __name__=="__main__":

    sprices = (5, 3, 2, 10, 12, 15, 17, 11, 6, 8 , 10, 20, 23, 17, 15, 16, 18, 20, 26, 50,
               13, 24, 45, 49, 25, 23, 27, 31, 25)
    sp = stock_prices(list(sprices))

    mpo = sp.max_profit_once()
    print ("MAX PROFIT ONCE")
    mpo.print()

    maxprofit, mpu = sp.max_profit_unlimited()

    print("\n\nMAX PROFIT UNLIMITED TRADES")
    print("Total Profit = {}".format(maxprofit))

    maxprofit, al = sp.max_profit_all()

    print("\n\nMAX PROFIT ALL (UNLIMITED TRADES)")
    print("Total Profit = {}".format(maxprofit))
    for index in al:
        print("LOCAL MAX/MIN POINT INDEX = {} PRICE = {}".format(index, sp[index]))
    sp.print_bplist()

    n = 1
    maxprofit, al = sp.max_profit_limited(n)

    print("\n\nMAX PROFIT {} TRADE".format(n))
    print("Total Profit = {}".format(maxprofit))
    for index in al:
        print("LOCAL MAX/MIN POINT INDEX = {} PRICE = {}".format(index, sp[index]))
    sp.print_bplist()

    n = 3
    maxprofit, al = sp.max_profit_limited(n)

    print("\n\nMAX PROFIT {} TRADES".format(n))
    print("Total Profit = {}".format(maxprofit))
    for index in al:
        print("LOCAL MAX/MIN POINT INDEX = {} PRICE = {}".format(index, sp[index]))
    sp.print_bplist()

    n = 2
    maxprofit, al = sp.max_profit_limited(n)

    print("\n\nMAX PROFIT {} TRADES".format(n))
    print("Total Profit = {}".format(maxprofit))
    for index in al:
        print("LOCAL MAX/MIN POINT INDEX = {} PRICE = {}".format(index, sp[index]))
    sp.print_bplist()

