class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        processed = set()
        heap = [(-1, start_node)]

        while heap:
            curr_dist, curr_node = heappop(heap)
            processed.add(curr_node)

            if curr_node == end_node:
                return curr_dist * -1
            
            for child, weight in graph[curr_node]:
                if child not in processed:
                    heappush(heap, (curr_dist * weight, child))
        
        return 0