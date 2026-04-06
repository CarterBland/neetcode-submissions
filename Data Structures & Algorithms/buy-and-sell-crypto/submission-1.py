class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lowestPrice = prices[0]

        for price in prices:
            lowestPrice = min(price, lowestPrice)
            best = max(price - lowestPrice, best)

        return best