from collections import defaultdict

flag = 0

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def depthLimitedSearch(self, src, target, maxDepth):
        visited = defaultdict(bool)
        path = []
        self.depthLimitedSearchUtil(src, target, maxDepth, visited, path)

    def depthLimitedSearchUtil(self, src, target, maxDepth, visited, path):
        visited[src] = True
        path.append(src)

        # print("visited:", visited[src])
        # print("src", src)
        # print("self. graph", self.graph)
        # print("path", path)

        if src == target:
            print(path)
            global flag
            flag = 1

        elif maxDepth > 0:
            for i in self.graph[src]:
                if visited[i] == False:
                    self.depthLimitedSearchUtil(i, target, maxDepth - 1, visited, path)

        path.pop()
        visited[src] = False

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(1, 6)
g.addEdge(3, 6)
g.addEdge(9, 8)

source = int(input("Masukkan lokasi: "))
target = int(input("Masukkan tujuan: "))
limit = int(input("Masukkan limit: "))

g.depthLimitedSearch(source, target, limit)

if (flag == 1):
    print("Titik terhubung")
else:
    print("Titik tidak terhubung")
