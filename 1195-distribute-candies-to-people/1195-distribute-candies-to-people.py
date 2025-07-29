class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        res, i = [0] * n, 0
        while candies > 0:
            loss = min(candies, i + 1)
            res[i % n] += loss
            candies -= loss
            i += 1
        return res