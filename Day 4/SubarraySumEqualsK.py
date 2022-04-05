class Solution:
    def subarraySum(self, arr: list[int], target: int) -> int:
        count = 0
        prefixSum = {0:1}
        
        currSum = 0
        for i in arr:
            currSum += i
            count += prefixSum.get(currSum-target, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
            
        return count