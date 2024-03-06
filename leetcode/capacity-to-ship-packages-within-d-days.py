class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacity(days, mid):
            sum = 0
            count = 0
            right = 0
            while right < len(weights):
                while right < len(weights) and sum + weights[right] <= mid:
                    sum += weights[right]
                    right += 1
                count += 1
                sum = 0
            if count > days:
                return False
            return True

        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if capacity(days, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low