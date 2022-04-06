import collections
class TimeMap:
    
    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            arr = self.d[key]
            
        if not self.d[key]:
            return ""
        
        if timestamp > arr[-1][0]:
            return arr[-1][1]
        
        if timestamp < arr[0][0]:
            return ""
        
        low = 0
        high = len(arr)-1
        
        while low <= high:
            mid = (low+high)//2
            if arr[mid][0] > timestamp:
                high  = mid - 1
            else:
                low = mid + 1
                
        if low < len(arr)-1:
            return arr[low][1]
        
        else:
            return arr[high][1]