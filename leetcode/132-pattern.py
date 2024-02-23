class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        rightBest = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < rightBest:
                    return True
            while stack and stack[-1] < nums[i]:
                num = stack.pop()
                rightBest = max(rightBest, num)
            stack.append(nums[i])
        return False