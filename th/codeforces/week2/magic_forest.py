import sys

def countDistinctXorangles(n):
    ans = 0
    for a in range(1, n, 1):
        for b in range(a + 1, n, 1):
            c = a ^ b
            if a + b > c and c > b - a and n >= c and c > b:
                ans += 1
                # print(a, b, c)
        
    return ans

n = int(sys.stdin.readline())
print(countDistinctXorangles(n))