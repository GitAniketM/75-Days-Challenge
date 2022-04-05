import collections
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        c = collections.defaultdict(int)
        c[0] = 1
        prefixSum = 0
        
        count = 0
        
        for i in nums:
            prefixSum += i
            
            if prefixSum % k in c:
                count += c[prefixSum % k]
            
            c[prefixSum % k] += 1
            
        return count