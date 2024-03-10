class Solution:
    def smallestNumber(self, num: int) -> int:
        n = list(str(num))
        if num > 0:
            n.sort()
            zeros = n.count("0")
            removed = [x for x in n if x != "0"]
            for i in range(zeros):
                removed.insert(1, "0")
            return int("".join(removed))
        elif num < 0:
            removed = n[1:]
            removed.sort(reverse = True)
            return int("".join(removed)) * -1
        else:
            return 0