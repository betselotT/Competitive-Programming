class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:  
            return True

        left, right = 0, 0
        while right < len(t):
            if s[left] == t[right]:
                left += 1
                if left == len(s):
                    return True
            right += 1
        
        return False
