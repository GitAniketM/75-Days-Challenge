import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r=-1
        d = collections.Counter()

        for r,v in enumerate(s):
          	
            d[v]+=1
            max_char_count = max(d.values())
            if (r +1 - l) - max_char_count > k:
                d[s[l]] -= 1
                l += 1
        return r+1-l