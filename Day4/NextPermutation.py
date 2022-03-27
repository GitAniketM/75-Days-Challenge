class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        n = len(nums)
        
        i = n-1
        while i > 0:
            if nums[i] > nums[i-1]:
                idx = i
                break
            i -= 1
            
        if idx == -1:
            nums.reverse()
        else:
            prev = idx
            for i in range(idx+1, n):
                if (nums[i] > nums[idx-1] and nums[i] <= nums[prev]):
                    prev = i
            nums[idx-1], nums[prev] = nums[prev], nums[idx-1]
            
            arr = nums[:idx]+nums[idx:][::-1]
            nums.clear()
            nums.extend(arr)