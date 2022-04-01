class Solution:
    def canJump(self, arr: list[int]) -> bool:
        index = 0
        if len(arr) == 1 and arr[0] == 0:
            return True
        for i in range(len(arr)):
            if arr[i] == 0 and index <= i and i!= len(arr)-1:
                return False
            index = max(index, i+arr[i])
        if index >= len(arr)-1:
            return True
        else:
            return False