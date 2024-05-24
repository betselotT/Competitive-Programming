class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, i):
            if i >= len(word):
                return node.is_end
            if word[i] != ".":
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)
            else:
                for c in node.children.values():
                    if dfs(c, i + 1):
                        return True
                return False
        return dfs(curr, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)