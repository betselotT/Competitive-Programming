class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        for i in range(len(points)):
            arr.append(points[i][0])
        arr.sort()
        ans = []
        for i in range(len(arr) - 1):
            widest = abs(arr[i + 1] - arr[i])
            ans.append(widest)
            print(widest)
        return max(ans)