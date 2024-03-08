class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        front, back = [], []
        var = 0
        for i in range(len(nums)):
            var += nums[i]
            front.append(var)
        var = 0
        for i in range(len(nums) - 1, -1, -1):
            var += nums[i]
            back.append(var)
        back.reverse()
        left, right = 0, 0
        for _ in range(len(nums)):
            if front[left] != back[right]:
                left += 1
                right += 1
            else:
                return left
        return -1