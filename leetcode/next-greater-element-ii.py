class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        arr = [-1] * len(nums) 
        n = len(nums)
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                num = stack.pop()
                arr[num] = nums[i % n]
            stack.append(i % n)
        return arr
