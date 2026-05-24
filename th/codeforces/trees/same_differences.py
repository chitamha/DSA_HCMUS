import sys
write = sys.stdout.write

def solve():
    q = int(sys.stdin.readline())
    for _ in range(q):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        count, ans = [0] * (2*n + 5), 0
        for i in range(n):
            ans += count[arr[i] - i + n]
            count[arr[i] - i + n] += 1
        write(f"{ans}\n")

if __name__ == "__main__":
    solve()
