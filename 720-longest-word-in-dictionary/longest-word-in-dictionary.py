class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        
        curr.is_end = True
    
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            
            if word[i] in node.children and node.children[word[i]].is_end:
                return dfs(node.children[word[i]], i + 1)

            return False
        
        return dfs(self.root, 0)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        ans = []
        for w in words:
            t.insert(w)
        
        for w in words:
            if t.search(w):
                ans.append(w)
        
        temp = ""
        for w in ans:
            if len(w) == len(temp):
                if temp > w:
                    temp = w
            elif len(w) > len(temp):
                temp = w
                
        return temp