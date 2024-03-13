class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        bucket = []
        parents = ("(" * n) + (")" * n)
        counter = 0   
        def backtrack(j, counter):
            if counter == 0 and len(bucket) == 2*n:
                ans.add("".join(bucket[:]))     
                return
            if counter > n or counter < 0 or len(bucket) > 2*n:
                return
            val = None
            for j in range(len(parents)):
                if parents[j] != val:
                    bucket.append(parents[j])
                    backtrack(j+1, counter + (1 if parents[j] == "(" else -1))
                    val = bucket.pop()
        backtrack(0,0)
        return list(ans)