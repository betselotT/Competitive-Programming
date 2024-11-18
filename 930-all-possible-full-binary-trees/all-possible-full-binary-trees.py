class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {
            1: [TreeNode()]
        }

        if n % 2 == 0:
            return []

        def helper(n):
            if n < 0:
                return []

            if n in dp:
                return dp[n]

            dp[n] = []
            
            l, r = 1, n - 2

            while r > 0 and l < n - 1:
                dp[n] += [TreeNode(0, i, j) for i in helper(l) for j in helper(r)]
                l += 2
                r -= 2
            
            return dp[n]
              
        return helper(n)