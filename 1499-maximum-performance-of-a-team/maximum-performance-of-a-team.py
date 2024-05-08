class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        checker = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        summ, maxx = 0, 0

        for e, s in checker:
            if len(heap) == k:
                summ -= heappop(heap)
            heappush(heap, s)
            summ += s
            maxx = max(maxx, summ * e)
            
        return maxx % MOD