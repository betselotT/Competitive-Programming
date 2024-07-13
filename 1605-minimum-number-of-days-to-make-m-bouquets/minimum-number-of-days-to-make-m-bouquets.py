class Solution:
    def minDays(self, bloom_days: List[int], m: int, k: int) -> int:
        if m * k > len(bloom_days): 
            return -1
        def is_valid(day_number) -> bool:
            cur_bloom = 0
            cur_bouquets = 0
            for i in range(len(bloom_days)):
                if day_number < bloom_days[i]:
                    cur_bloom = 0 
                else:
                    cur_bloom += 1 
                    if cur_bloom == k:
                        cur_bloom = 0
                        cur_bouquets += 1
                        if cur_bouquets >= m: return True
            return False
        timers = sorted(list(Counter(bloom_days).keys()))
        left, right = 0, len(timers) - 1
        optimal_day = 0
        while left <= right:
            mid = left + (right-left)//2
            if is_valid(timers[mid]):
                optimal_day = mid
                right = mid - 1
            else:
                left = mid + 1
        return timers[optimal_day]