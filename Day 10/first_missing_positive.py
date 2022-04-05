class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        temp = 1
        v = set(nums)
        
        if temp not in v:
            return temp
        i = 0
        while i < len(nums):
            if temp not in v:
                return temp
            elif temp in v:
                temp += 1
                
            i += 1
        return temp