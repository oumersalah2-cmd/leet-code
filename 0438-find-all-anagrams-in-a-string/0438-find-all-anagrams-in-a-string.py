from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_count = Counter(p)
        window_count = Counter()
        
        k = len(p)
        
        for i in range(len(s)):
            window_count[s[i]] += 1
            
            if i >= k:
                if window_count[s[i - k]] == 1:
                    del window_count[s[i - k]]
                else:
                    window_count[s[i - k]] -= 1
            
            if window_count == p_count:
                result.append(i - k + 1)
        
        return result