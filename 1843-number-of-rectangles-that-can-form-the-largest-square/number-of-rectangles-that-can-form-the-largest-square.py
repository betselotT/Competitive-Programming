class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        rects = defaultdict(int)

        for a, b in rectangles:
            rects[min(a, b)] += 1

        ans = 0
        maxFreq = 0

        for k, v in rects.items():
            if k > maxFreq:
                maxFreq = k
                ans = v

        return ans