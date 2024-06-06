class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dp(i):
            if len(path) == len(s):
                res.append("".join(path.copy()))
                return
            if s[i].isdigit():
                path.append(s[i])
                dp(i + 1)
                path.pop()
            else:
                path.append(s[i].lower())
                dp(i + 1)
                path.pop()
                path.append(s[i].upper())
                dp(i + 1)
                path.pop()
        res = []
        path = []
        dp(0)
        return res