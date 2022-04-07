class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.getcount(nums,k) - self.getcount(nums,k-1)
    def getcount(self,nums,k):
        count = 0
        l,r = 0,0
        d = {}
        
        while l < len(nums):
            d[nums[l]] = d.get(nums[l],0)+1
            
            while len(d) > k:
                d[nums[r]] -= 1
                if d[nums[r]] == 0:
                    d.pop(nums[r])
                    
                r += 1
            count += (l-r+1)
            l += 1
            
        return count