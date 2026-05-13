import sys

write = sys.stdout.write

def main():
    n = int(input())
    diary = set()
    for _ in range(n):
        name = input()
        if name in diary:
            write("YES\n")
        else:
            write("NO\n")
            diary.add(name)

if __name__ == "__main__":
    main()