class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, nums):
        curr = self.root
        for i in range(32, -1, -1):
            bit = 1 if nums & (1<<i) else 0
            if curr.children[bit] == None:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

    def search(self, num):
        maxx = 0
        curr = self.root
        for i in range(32, -1, -1):
            bit = 1 if num & (1<<i) else 0
            if curr.children[1 - bit]:
                curr = curr.children[1 - bit]
                maxx = maxx | (1<<i)
            else:
                curr = curr.children[bit]
        return maxx

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie()
        for num in nums:
            t.insert(num)
        ans = 0
        for num in nums:
            a = t.search(num)
            ans = max(ans, a)
        
        return ans