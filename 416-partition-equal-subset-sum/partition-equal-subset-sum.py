class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(bool)
        def check(i , target):
            if target == 0:
                return True
            if i == len(nums):
                return False

            if (i, target) not in memo:
                memo[(i, target)] = check(i + 1, target - nums[i]) or check(i + 1, target)

            return memo[(i, target)]

        summ = sum(nums)
        if summ % 2 != 0:
            return False

        return check(0, summ // 2)