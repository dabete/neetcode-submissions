class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input - integer array 'prices'

        max_profit = 0

        left = 0
        if len(prices) == 1:
            return 0
        else:
            right = 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_profit
        