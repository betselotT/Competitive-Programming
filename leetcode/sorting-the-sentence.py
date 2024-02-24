class Solution:
    def sortSentence(self, s: str) -> str:
        newArr = []
        new = s.split()
        arr = [item[-1] + item[:-1] for item in new]
        arr.sort()
        ans = [item[1:] for item in arr]
        return " ".join(ans)
            