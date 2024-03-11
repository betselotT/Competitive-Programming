class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        alice = 0
        me = 0
        bob = 0
        piles.sort(reverse=True)
        while piles:
            alice += piles.pop(0)
            me += piles.pop(0)
            bob += piles.pop()
        return me