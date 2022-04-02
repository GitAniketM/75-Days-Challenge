class Solution:
    def largestRectangleArea(self, h: list[int]) -> int:
        l, stack = [], []
        for i in range(len(h)):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            if stack == []:
                l.append(0)
            else:
                l.append(stack[-1]+1)
            stack.append(i)
            
        stack = []
        maxi = 0
        n = len(h)
        for i in range(n-1, -1, -1):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            if stack == []:
                r = n-1
            else:
                r = stack[-1]-1
            
            stack.append(i)
            maxi = max(maxi, (r-l[i]+1)*h[i])
            
        return maxi