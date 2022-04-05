import heapq
class Solution:
    def maxScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        k1 = n-k
        
        curr = 0
        inf = 10**9
        min_current = inf
        summ=0
        
        for i in range(n):
            if i >= k1:
                curr -= nums[i-k1]
            curr += nums[i]
            if i >= k1-1:
                min_current = min(min_current , curr)
            summ += nums[i]
        
        if min_current == inf:
            return summ
        
        return summ - min_current
    