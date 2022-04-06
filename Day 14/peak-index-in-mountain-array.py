class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return i