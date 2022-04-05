class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        i, j = 0,1
        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i = j
            else:
                diff = prices[j] - prices[i]
                total += diff
                i += 1
            j += 1
        return total