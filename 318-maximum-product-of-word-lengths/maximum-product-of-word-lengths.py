class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = []
        for w in words:
            res.append(set(w))
            
        maxx= 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not res[i] & res[j]:
                    maxx = max(maxx, len(words[j]) * len(words[i]))
        return maxx