class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        mask = 0
        count[0] = 1
        result = 0
        
        for c in word:
            mask ^= 1 << (ord(c) - ord('a'))
            result += count[mask]
            for i in range(10):
                result += count[mask ^ (1 << i)]
            count[mask] += 1
            
        return result