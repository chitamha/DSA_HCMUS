import sys

def main():
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    frontColor = list(map(int, sys.stdin.readline().split()))
    backColor = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    favouriteColors = list(map(int, sys.stdin.readline().split()))

    colors = [[] for _ in range(4)]
    for i in range(n):
        if frontColor[i] != backColor[i]:
            colors[frontColor[i]].append(i)
            colors[backColor[i]].append(i)
        else:
            colors[backColor[i]].append(i)

    for i in range(1, 4):
        colors[i].sort(key = lambda x : prices[x])
        # print(colors[i])

    pointerColors = [0] * 4
    isBought = [0] * n

    for i in range(m):
        favouriteColor = favouriteColors[i]
        while pointerColors[favouriteColor] < len(colors[favouriteColor]) and isBought[colors[favouriteColor][pointerColors[favouriteColor]]] == 1:
            pointerColors[favouriteColor] += 1
        
        if pointerColors[favouriteColor] < len(colors[favouriteColor]):
            if isBought[colors[favouriteColor][pointerColors[favouriteColor]]] == 0:
                print(prices[colors[favouriteColor][pointerColors[favouriteColor]]], end = " ")
                isBought[colors[favouriteColor][pointerColors[favouriteColor]]] = 1
            else:
                print(-1, end = " ")
        else:
            print(-1, end = " ")

main()