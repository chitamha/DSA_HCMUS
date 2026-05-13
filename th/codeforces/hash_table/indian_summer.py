import sys

write = sys.stdout.write

def main():
    n = int(input())
    leaves = {}
    for _ in range(n):
        leaf = input()
        if leaf in leaves:
            continue
        else:
            leaves[leaf] = 1
    write(str(len(leaves)))

if __name__ == "__main__":
    main()