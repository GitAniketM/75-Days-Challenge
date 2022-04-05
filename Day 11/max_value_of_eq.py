class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        hq = []
        maxi = -math.inf
        for x, y in points:
            while hq and hq[0][1] < x-k:
                heapq.heappop(hq)
            if hq:
                maxi = max(maxi, -hq[0][0]+y+x)
            heapq.heappush(hq, (x-y, x))
        
        return maxi
        