class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = {n: float('inf') for n in range(1, n + 1)}
        distances[k] = 0
        processed = set()
        heap = [(0, k)]

        while heap:
            curr_dist, curr_node = heappop(heap)
            if curr_node in processed:
                continue
            processed.add(curr_node)

            for child, weight in graph[curr_node]:
                distance = curr_dist + weight
                if distance < distances[child]:
                    distances[child] = distance
                    heappush(heap, (distance, child))

        if len(processed) == n:
            return max(distances.values())
        else:
            return -1