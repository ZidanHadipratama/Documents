from typing import List

class Solution:
    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float('inf')] * n for _ in range(n)]
        for u, v, wt in edges:
            graph[u][v] = wt
            graph[v][u] = wt

        neighbor_count = [0] * n

        def dfs(city, visited, dist):
            visited[city] = True
            for neighbor in range(n):
                if not visited[neighbor] and graph[city][neighbor] <= dist:
                    dfs(neighbor, visited, dist)

        for city in range(n):
            visited = [False] * n
            dfs(city, visited, distanceThreshold)
            neighbor_count[city] = sum(visited) - 1  

        min_neighbors = float('inf')
        result_city = -1
        for city in range(n):
            if neighbor_count[city] < min_neighbors:
                min_neighbors = neighbor_count[city]
                result_city = city
            elif neighbor_count[city] == min_neighbors:
                result_city = max(result_city, city) 

        return result_city

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    edges = []
    for i in range(m):
        u, v, wt = map(int, input().strip().split())
        edges.append([u, v, wt])
    distanceThreshold = int(input().strip())
    obj = Solution()
    ans = obj.findCity(n, m, edges, distanceThreshold)
    print(ans)
