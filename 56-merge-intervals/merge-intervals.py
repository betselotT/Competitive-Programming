class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        ans = []
        intervals.sort()

        check = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= check[1]:
                check[1] = max(check[1], interval[1])
            else:
                ans.append(check)
                check = interval
        
        ans.append(check)

        return ans