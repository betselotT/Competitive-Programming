class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def capacity(h, mid):
            count = 0
            for i in range(len(piles)):
                if piles[i] < mid:
                    count += 1
                else:
                    count += ceil((piles[i] / mid))
            if count > h:
                return False
            return True

        low = 1
        high = sum(piles)
        while low <= high:
            mid = (low + high) // 2
            if capacity(h, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low