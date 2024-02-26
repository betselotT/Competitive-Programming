class Solution:
    def reverseStr(self, s, start, end):
        if start >= end:
            return
        s[start], s[end] = s[end], s[start]
        self.reverseStr(s, start + 1, end - 1)
        
    
    def reverseString(self, s: List[str]) -> None:
        self.reverseStr(s, 0, len(s) - 1)