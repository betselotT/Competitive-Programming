class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        to_remove = 0
        for symb in s[::-1]:
            if symb == "*":
                to_remove += 1
            else:
                if not to_remove:
                    res += symb
                else:
                    to_remove -= 1
        return res[::-1]