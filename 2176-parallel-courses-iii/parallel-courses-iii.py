class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        next = {node: [] for node in range(n)}
        nodeToPrev = {node: 0 for node in range(n)}
        for prev, nextt in relations:
            next[prev-1].append(nextt-1)
            nodeToPrev[nextt-1] += 1
        
        heap = []
        for node, count in nodeToPrev.items():
            if count == 0:
                heappush(heap, (time[node], node))
        
        while heap:
            ans, node = heappop(heap)
            for nextt in next[node]:
                nodeToPrev[nextt] -= 1
                if nodeToPrev[nextt] == 0:
                    heappush(heap, (ans + time[nextt], nextt))
        
        return ans