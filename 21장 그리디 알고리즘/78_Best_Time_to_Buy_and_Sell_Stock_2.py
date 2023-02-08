class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for cur in prices:
            if cur < min_price:
                min_price = cur
                continue
            if cur > min_price:
                profit += (cur - min_price)
                min_price = cur

        return profit
      
