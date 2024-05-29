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

    def search(self, word: str) -> str:
        curr = self.root
        ans = ""
        for w in word:
            if w in curr.children:
                curr = curr.children[w]
                ans += w
                if curr.is_end:
                    return ans
            else:
                break

        return word
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for w in dictionary:
            t.insert(w)
        
        check = sentence.split()
        result = []
        for i in check:
            result.append(t.search(i))
        
        return " ".join(result)