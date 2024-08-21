class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ss = {char: index for index, char in enumerate(s)}
        tt = {char: index for index, char in enumerate(t)}
        ans = 0
        
        for char in s:
            ans += abs(ss[char] - tt[char])
        
        return ans
