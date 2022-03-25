class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        i = 1
        while i < len(prices):
            maxi = max(maxi, prices[i] - mini)
            mini = min(mini, prices[i])
            i += 1           
        return maxi