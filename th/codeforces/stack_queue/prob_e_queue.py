import sys

def swapPeople(n, list):
    list.sort()

    cnt, cur_sum = 0, 0
    for i in range(n):
        if cur_sum <= list[i]:
            cnt += 1
            cur_sum += list[i]
    
    print(cnt)

n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().split()))
swapPeople(n, list)