class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        l = 0
        maxx = 0
        merge = []
        for i in range(len(profit)):
            merge.append((profit[i], difficulty[i]))
        merge.sort(reverse = True)

        worker.sort(reverse = True)
        right = 0
        while right < len(worker):
            while l < len(merge) and merge[l][1] > worker[right]:
                l += 1
            if l < len(merge):
                maxx += merge[l][0]
            right += 1

        return maxx