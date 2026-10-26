class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        r = 0
        l = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

            if prices[r] < prices[l]:
                l = r

            r+=1

        return maxProfit
            
        