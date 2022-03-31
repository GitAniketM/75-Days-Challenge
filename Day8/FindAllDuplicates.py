from collections import Counter
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        d = Counter(nums)
        
        for k,v in d.items():
            if v > 1:
                res.append(k)
                
        return res