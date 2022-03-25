class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(arr):
            d[v] = i
            
        for i in range(len(arr)):
            diff = target - arr[i]
            if diff in d.keys() and d[diff] != i:
                return [i,d[diff]]
            