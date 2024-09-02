class Solution:
    def countPoints(self, rings: str) -> int:
        dictt = defaultdict(set)
        for i in range(1, len(rings), 2):
            dictt[rings[i]].add(rings[i - 1])
        
        count = 0
        for colors in dictt.values():
            if len(colors) == 3:  
                count += 1
        
        return count