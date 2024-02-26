class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = moves = 0
        for i in s:
            if i == '(':
                left += 1
            else:
                if right < left:
                    right += 1
                else:
                    moves += 1
        moves += left - right
        return moves