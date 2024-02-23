class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        start = points[0]
        count = 1
        for l, r in points[1:]:
            if l > start[1]:
                count += 1
                start = [l, r]
            else:
                start[1] = min(start[1], r)
        return count
        