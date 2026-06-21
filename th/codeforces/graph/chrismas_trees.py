import sys
import queue
write = sys.stdout.write
BASE = int(2e9)

def solve(n, m, coordinateX):
    minDis, ansList = 0, []
    marked, inserted = set(), set()
    q = queue.Queue()
    for x in coordinateX:
        x += BASE
        q.put((x, x))
        marked.add(x)
        inserted.add(x)

    while not q.empty() and len(ansList) < m:
        top, ancestor = q.get()
        if not (top in marked):
            ansList.append(top)
            minDis += abs(ancestor - top)

        if not (top - 1 in inserted):
            q.put((top - 1, ancestor))
            inserted.add(top - 1)
        if not (top + 1 in inserted):
            q.put((top + 1, ancestor))
            inserted.add(top + 1)

    write(f"{minDis}\n{' '.join(str(y - BASE) for y in ansList)}\n")

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    coordinateX = list(map(int, sys.stdin.readline().split()))
    solve(n, m, coordinateX)