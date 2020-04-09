class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0

        # check if all items are equal
        count = 0
        for x in prices:
            if x != prices[0]:
                count = 1
                break
        if not count:
            return 0

        lastBuy = prices[0]
        lastSale = -1
        buy = True
        profit = 0

        for i in range(1, len(prices)):
            if buy:
                if prices[i] <= lastBuy:
                    lastBuy = prices[i]
                else:
                    profit += prices[i] - lastBuy
                    lastSale = prices[i]
                    buy = False

            if not buy:
                if prices[i] > lastSale:
                    profit += prices[i] - lastSale
                    lastSale = prices[i]
                else:
                    lastBuy = prices[i]
                    buy = True

        return profit