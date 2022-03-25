class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        for i in digits:
            arr.append(str(i))
        digit = int("".join(arr))
        digit += 1
        digit = str(digit)
        return list(map(int, digit))
    