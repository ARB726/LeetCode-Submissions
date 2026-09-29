class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        goodProfit = 0
        minPrice = float('inf')
        for price in prices:

            minPrice = min(minPrice , price)
            profit = price - minPrice

            goodProfit = max(profit , goodProfit)

        return goodProfit