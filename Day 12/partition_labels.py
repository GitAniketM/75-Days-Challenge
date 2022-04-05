class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        d = {}
        for i, c in enumerate(s):
            d[c]=i
        
        
        res = []
        size = 0
        end = 0
        for i,c in enumerate(s) :
            size+=1
            if d[c] > end:
                end = d[c]
            
            if i==end:
                res.append(size)
                size=0
                
        return res