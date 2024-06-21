class Solution:
    def findOriginalArray(self, changed):
        count = Counter(changed)
        ans = []
        if len(changed) % 2: 
            return []

        for x in sorted(count.keys()):
            if count[x] > count[x* 2]: 
                return []
            if x == 0:
                if count[x] % 2:
                    return []
                else: 
                    ans += [0] * (count[x] // 2)
            else:
                ans += [x] * count[x]
            count[2 * x] -= count[x]

        return ans