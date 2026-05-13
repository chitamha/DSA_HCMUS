import sys

write = sys.stdout.write

def main():
    n, m = map(int, input().split())
    severs = dict()

    for _ in range(n):
        line = input().split()
        severs[line[1]] = line[0]
    
    for _ in range(m):
        line = input().split()
        write(f"{' '.join(line)} #{severs[line[1][:-1]]}\n")

if __name__ == "__main__":
    main()