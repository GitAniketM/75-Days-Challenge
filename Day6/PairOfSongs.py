class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = {}
        count = 0
        
        for i in range(len(time)):
            remainder = time[i] % 60
            diff = 60 - remainder
            
            if remainder == 0:
                if remainder in pairs:
                    count += pairs[remainder]
                
            elif diff in pairs:
                count += pairs[diff]
            
            if remainder in pairs:
                pairs[remainder] += 1
            else:
                pairs[remainder] = 1
                
        return count
                