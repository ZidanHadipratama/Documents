from typing import List

class Solution:
    def findShortestPath(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])

        mud_holes = []
        path = []
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    mud_holes.append((i, j))
                    if i+1>0 and i+1<r:
                        mud_holes.append((i+1, j)) 
                    if i-1>=0 and i-1<r:
                        mud_holes.append((i-1, j)) 
                    if j+1>=0 and j+1<r:
                        mud_holes.append((i, j+1)) 
                    if j-1>=0 and j-1<r:
                        mud_holes.append((i, j-1)) 

        for i in range(r):
            for j in range(c):
                if (i, j) in mud_holes:
                    continue
                else:
                    path.append((i, j))

        def is_valid(row, col, chosen_nodes):
            return (row, col) in chosen_nodes

        def get_neighbors(row, col):
            return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        def find_all_paths(chosen_nodes, current_node, target_col, visited, path, all_paths):
            row, col = current_node

            if col == target_col:
                all_paths.append(path)
                return

            for neighbor_row, neighbor_col in get_neighbors(row, col):
                neighbor_node = (neighbor_row, neighbor_col)
                if is_valid(neighbor_row, neighbor_col, chosen_nodes) and neighbor_node not in visited:
                    visited.add(neighbor_node)
                    find_all_paths(chosen_nodes, neighbor_node, target_col, visited, path + [neighbor_node], all_paths)
                    visited.remove(neighbor_node)

        def shortest_path_from_col0(chosen_nodes):
            start_nodes_col0 = [(row, col) for row, col in chosen_nodes if col == 0]

            if not start_nodes_col0:
                return -1

            all_paths = []
            for start_node in start_nodes_col0:
                visited = set([start_node])
                find_all_paths(chosen_nodes, start_node, 4, visited, [start_node], all_paths)

            if not all_paths:
                return -1

            shortest_path = min(all_paths, key=len)
            return int(len(shortest_path))
        
        return shortest_path_from_col0(path)

# Contoh penggunaan
if __name__ == "__main__":
    rows, cols = map(int, input().strip().split())
    mat = [list(map(int, input().strip().split())) for _ in range(rows)]
    obj = Solution()
    res = obj.findShortestPath(mat)
    print(res)
