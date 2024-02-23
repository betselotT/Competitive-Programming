class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        mySet = set()
        for i, j in ranges:
            for k in range(i, j+1):
                mySet.add(k)
        while left <= right:
            if left not in mySet:
                return False
            left += 1
        return True