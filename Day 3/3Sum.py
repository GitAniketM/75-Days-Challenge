class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[i]+nums[j]+nums[k]
                if(s == 0):
                    result.append((nums[i],nums[j],nums[k]))
                    j += 1
                if s < 0:
                    j += 1
                else:
                    k -= 1
        return (list(set(result)))