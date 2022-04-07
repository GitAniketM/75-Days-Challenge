import collections
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]
        
        result = []
        d = collections.defaultdict(list)
        for i,v in enumerate(nums):
            d[v].append(i)
            
        if target not in d:
            return [-1,-1]
        else:
            result.append(d[target][0])
            result.append(d[target][-1])
            return result