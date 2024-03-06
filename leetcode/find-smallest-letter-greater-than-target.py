class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = bisect_right(letters, target)
        if ans == len(letters):
            return letters[0]
        return letters[ans]