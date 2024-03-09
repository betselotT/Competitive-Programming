class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best = ""
        def good(i, j):
            t = set(s[i:j])
            for i in t:
                if (i.lower() in t) != (i.upper() in t):
                    return False
            return True
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if good(i, j) and j - i > len(best):
                    best = s[i:j]
        return best