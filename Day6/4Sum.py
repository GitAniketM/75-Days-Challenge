class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                low = j+1
                high = len(nums)-1
                while low < high:
                    arr = [nums[i], nums[j], nums[low], nums[high]]
                    summ = sum(arr)
                    if summ == target:
                        if arr not in res:
                            res.append(arr)
                        low += 1
                    elif summ < target:
                        low += 1
                    else:
                        high -= 1
        return res