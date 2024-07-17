class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        decrement, result = 0, 0
        while (k > 0 and happiness[decrement]-decrement > 0):
            result += happiness[decrement]-decrement
            k, decrement = k-1, decrement+1
        return result