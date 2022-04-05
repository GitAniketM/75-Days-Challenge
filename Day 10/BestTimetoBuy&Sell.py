class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0:
            return 0
        
        dp = [[0]*len(prices) for _ in range(3)]
        
        for i in range(1,3):
            mini = prices[0]
            for j in range(1,len(prices)):
                mini = min(mini, prices[j] - dp[i-1][j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] - mini)
                
        return dp[2][len(prices)-1]