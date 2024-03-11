class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count, num = 0, 0
        for i in range(len(flips)):
            num = max(num, flips[i])
            if num == i + 1:
                count += 1
        return count