class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def calc(mid):
            left, right = 0, 0
            while left < len(houses) and right < len(heaters):
                if abs(houses[left] - heaters[right]) > mid:
                    right += 1
                else:
                    left += 1
            if left == len(houses):
                return True
            return False

        low = 0
        x = max(houses)
        y = max(heaters)
        high = max(x, y)
        while low <= high:
            mid = (low + high) // 2
            if calc(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low