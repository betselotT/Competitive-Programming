class Solution:
    def f(self, start, end, nums):
        j = start
        curr = 0
        prev = nums[start]
        prev2 = 0
        
        for i in range(start + 1, end + 1):
            pick = nums[i]
            if i > j + 1:
                pick += prev2
            skip = prev
            curr = max(pick, skip)
            prev2 = prev
            prev = curr
        return prev

    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.f(0, n - 2, nums), self.f(1, n - 1, nums))