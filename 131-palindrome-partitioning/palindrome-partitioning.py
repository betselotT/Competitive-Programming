class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def check(i):
            if i >= len(s):
                ans.append(part.copy())
                return 
            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    part.append(s[i:j + 1])
                    check(j + 1)
                    part.pop()
        
        check(0)
        return ans

    def palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True