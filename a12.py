def findShortestPath(mat):
    # Menghitung jumlah baris dan kolom
    r, c = len(mat), len(mat[0])
    
    # Fungsi bantuan untuk memeriksa apakah sel valid
    def isValid(x, y):
        return 0 <= x < r and 0 <= y < c
    
    # Menyimpan koordinat lubang lumpur
    mud_holes = []
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                mud_holes.append((i, j))
    
    # Inisialisasi queue BFS dengan posisi awal Alex
    queue = [(0, j) for j in range(c)]
    visited = set(queue)
    
    # Mulai BFS
    while queue:
        x, y = queue.pop(0)
        if y == c - 1:
            return x  # Alex mencapai tepi kanan, mengembalikan panjang rute
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if isValid(nx, ny) and (nx, ny) not in visited and mat[nx][ny] == 1:
                # Memastikan tidak ada lubang lumpur di sekitar
                valid = True
                for mx, my in mud_holes:
                    if abs(nx - mx) + abs(ny - my) <= 1:
                        valid = False
                        break
                if valid:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    
    return -1  # Tidak ada rute yang memungkinkan

# Contoh penggunaan
mat0 = [
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1]
]
print(findShortestPath(mat0))  # Output yang benar: -1

mat1 = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]
print(findShortestPath(mat1))  # Output yang benar: 6
