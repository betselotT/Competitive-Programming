class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum = 0
        while left < right:
            width = abs(right - left)
            h = min(height[left], height[right])
            area = width * h
            maximum = max(maximum, area)
            if height[left] < height[right]:
                left += 1 
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1 
        return maximum