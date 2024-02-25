class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num = target
        moves = 0
        while num != 1 and maxDoubles > 0:
            if num % 2 != 0:
                num -= 1
                moves += 1
            else:
                num //= 2
                moves += 1
                maxDoubles -= 1
        moves += (num - 1)
        return moves