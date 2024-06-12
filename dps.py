from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, max_depth):
        if src == target : return True
        if max_depth <= 0 : return False
        for i in self.graph[src]:
            if(self.DLS(i, target, max_depth-1)):
                return True
        return False

    def iterative_DLS(self, src, target, max_depth):
        for i in range(max_depth):
            if (self.DLS(src, target, i)):
                return True
        return False


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

target = 6; max_depth = 3; src = 0

if g.iterative_DLS(src, target, max_depth) == True:
    print("Target is reachable within max depth")
else :
    print("Target is NOT reachable within max depth")
