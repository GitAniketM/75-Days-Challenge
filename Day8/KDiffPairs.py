from collections import Counter
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        d = Counter(nums)
        count = 0
        
        if k == 0:
            for i in d:
                if d[i] > 1:
                    count += 1
        else:
            print(d)           
            for i in d:
                if k+i in d:
                    print((k+i,i))
                    count += 1
                
        return count