class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        temp = None
        i = 0
        for ch in typed:
            if i < len(name) and ch == name[i] :
                temp = ch
                i += 1
            elif ch == temp:
                continue
            else:
                return False
        return i == len(name)