class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
            curr.count += 1
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        ans = 0
        curr = self.root
        for w in word:
            if w in curr.children:
                curr = curr.children[w]
                ans += curr.count
            else:
                break
        
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        for w in words:
            t.insert(w)
        
        res = [0] * len(words)
        for i in range(len(words)):
            res[i] = t.search(words[i])
            
        return res