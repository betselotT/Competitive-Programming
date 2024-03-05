class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myDict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        arr = []
        path = []
        def backtrack(i):
            if len(path) == len(digits):
                arr.append(''.join(path[:]))
                return
            for j in myDict[digits[i]]:
                path.append(j)
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        if digits == "":
            return []
        else:
            return arr