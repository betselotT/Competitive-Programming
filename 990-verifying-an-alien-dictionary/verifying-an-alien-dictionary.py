from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for k in range(len(words) - 1):
            word1 = words[k]
            word2 = words[k + 1]
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if order.index(word1[i]) > order.index(word2[i]):
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True