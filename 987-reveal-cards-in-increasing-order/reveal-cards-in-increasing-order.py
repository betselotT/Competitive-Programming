class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque([i for i in range(n)])
        sortedDeck = sorted(deck)
        res = [0]*n
        j = 0

        while q:
            index = q.popleft()
            res[index] = sortedDeck[j]
            j+=1
            if q:
                ele = q.popleft()
                q.append(ele)

        return res