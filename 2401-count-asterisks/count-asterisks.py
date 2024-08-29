class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        ans = 0
        for i in s:
            if i == '|' and count == 0:
                count = 1
            elif i == '|' and count == 1:
                count = 0
            elif i == '*' and count == 0:
                ans += 1
        return ans