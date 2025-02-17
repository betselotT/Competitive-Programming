from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  
        
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - 20), i):  
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break 
        
        return dp[-1]