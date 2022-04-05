class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = []
        right_sum = [0]*len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            left_sum.append(total)
        print(left_sum)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            right_sum[i] += total
        print(right_sum)
        
        for i in range(len(left_sum)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
            
        