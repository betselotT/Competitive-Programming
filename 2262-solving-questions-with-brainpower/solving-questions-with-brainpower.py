class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = defaultdict(int)
        for i in range(len(questions) - 1, -1, -1):
            memo[i] = max(questions[i][0] + memo[i + 1 + questions[i][1]], memo[i + 1])
            
        return memo[0]

        def dp(i):
            if i >= len(questions):
                return 0

            if i not in memo:
                memo[i] = max(dp(i + 1), questions[i][0] + dp(i + 1 + questions[i][1]))
            
            return memo[i]
        
        return dp(0)