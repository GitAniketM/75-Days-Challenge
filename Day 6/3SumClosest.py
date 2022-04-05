class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        mini = float('inf')
        ans = 0
        for i in range(n-1):
            l, r = i+1, n-1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s > target: 
                    r -= 1
                elif s < target: 
                    l += 1
                else: 
                    return s
                if abs(target-s) < mini:
                    mini = abs(target-s)
                    ans = s
        
        return ans