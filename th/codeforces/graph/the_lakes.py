import sys
write = sys.stdout.write


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t_str = input_data[ptr]
    ptr += 1
    t = int(t_str)
    
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr+1])
        ptr += 2
        
        grid = []
        for i in range(n):
            grid.append([int(x) for x in input_data[ptr : ptr + m]])
            ptr += m
            
        max_vol = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    # BFS/DFS iterative to find lake volume
                    current_vol = 0
                    stack = [(i, j)]
                    current_vol += grid[i][j]
                    grid[i][j] = 0  # Mark as visited by setting to 0
                    
                    while stack:
                        r, c = stack.pop()
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > 0:
                                current_vol += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))
                    
                    if current_vol > max_vol:
                        max_vol = current_vol
        write(f"{max_vol}\n")


if __name__ == "__main__":
    solve()