class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = []
        prefix = 0 
        for i, ch in enumerate(s): 
            prefix += ord(ch)-97
            if (i+1) % k == 0: 
                ans.append(chr(97 + prefix%26))
                prefix = 0 
        return "".join(ans)