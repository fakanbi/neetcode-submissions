class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for price in prices:
            # profit = num - minimum buy num
            maxProfit = max(maxProfit, price - minBuy)
            minBuy = min(price, minBuy)
        return maxProfit