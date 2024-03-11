class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse = True)
        mx = 0
        for i in range(len(tasks)):
            mx = max(mx, processorTime[i // 4] + tasks[i])
        return mx