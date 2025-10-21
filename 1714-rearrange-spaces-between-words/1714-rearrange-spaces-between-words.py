class Solution:
    def reorderSpaces(self, text: str) -> str:
        splitted = text.split(" ")
        words = [w for w in splitted if w]
        spaces_total = len(splitted) - 1
        join = spaces_total // (len(words) - 1) if len(words) > 1 else 0
        res = (" " * join).join(words)
        return res + " " * (len(text) - len(res))