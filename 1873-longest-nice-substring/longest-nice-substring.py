class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best= ""
        for i in range(len(s)):
            for j in range(i+1 , len(s)+1):
                t = set(s[i:j])
                flag = True
                for x in t:
                    if (x.lower() in t) != (x.upper() in t):
                        flag = False
                        break
                if flag and j - i > len(best):
                    best = s[i:j]
        return best
