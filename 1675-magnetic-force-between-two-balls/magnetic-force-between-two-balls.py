class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(pos):
            balls = 0
            basket = -inf
            for b in position:
                if b - basket >= pos:
                    balls += 1
                    basket = b
                
            return balls >= m
        
        inf = 10 ** 20
        position.sort()
        left = 1
        right = position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        
        return left