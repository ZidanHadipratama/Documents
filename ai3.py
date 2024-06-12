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
        return "No valid start nodes in column 0."

    all_paths = []
    for start_node in start_nodes_col0:
        visited = set([start_node])
        find_all_paths(chosen_nodes, start_node, 4, visited, [start_node], all_paths)

    if not all_paths:
        return "No valid paths from column 0 to column 4."

    shortest_path = min(all_paths, key=len)
    return shortest_path

# Example usage:
chosen_nodes = [(0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 4), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2)]
result = shortest_path_from_col0(chosen_nodes)
print("Shortest path from column 0 to column 4:", result)
