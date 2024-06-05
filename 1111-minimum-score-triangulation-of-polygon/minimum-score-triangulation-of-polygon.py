class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if abs(i - j) < 2:
                return 0

            if (i,j) not in memo:
                app = float(inf)
                for k in range(i + 1 , j):
                    app = min(app , dp(i, k) + dp(k, j) + values[i] * values[j] * values[k])

                memo[(i,j)] = app

            return memo[(i,j)]

        return dp(0 , len(values) - 1) 