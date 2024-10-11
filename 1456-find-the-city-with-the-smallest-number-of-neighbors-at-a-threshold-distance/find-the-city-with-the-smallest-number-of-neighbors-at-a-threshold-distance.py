class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        ans = float('inf')
        maxx = 0

        for i in range(n):
            distances = {n: float('inf') for n in range(1, n + 1)}
            distances[i] = 0
            processed = set()
            heap = [(0, i)]

            while heap:
                curr_dist, curr_node = heappop(heap)
                if curr_node in processed:
                    continue

                processed.add(curr_node)

                for child, weight in graph[curr_node]:
                    distance = curr_dist + weight
                    if distance <= distanceThreshold:
                        distances[child] = distance
                        heappush(heap, (distance, child))
                
            if len(processed) <= ans:
                ans = min(ans, len(processed))
                maxx = max(maxx, i)

        return maxx