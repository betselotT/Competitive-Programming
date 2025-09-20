class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        count = 1
        for i in range(1, len(s), 1):
            if s[i] == s[i - 1]:
                count += 1
                ans = max(count, ans)
            else:
                count = 1
        return ans