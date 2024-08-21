class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii = []
        score = 0
        for i in s:
            ascii.append(ord(i))
        for i in range(1, len(ascii)):
            score += (abs(ascii[i] - ascii[i - 1]))
        
        return score