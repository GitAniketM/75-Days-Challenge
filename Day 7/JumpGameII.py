class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = [float('inf') for _ in range(n)]
        jumps[0] = 0
        
        for i in range(n):
            for j in range(1, nums[i]+1):
                if i + j < n:
                    jumps[i+j] = min(jumps[i+j], jumps[i]+1)
                    
        return jumps[-1]