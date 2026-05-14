import sys

write = sys.stdout.write

def main():
    n = int(input())
    f = {"polycarp": 1}
    for _ in range(n):
        line = input().split()
        line[0] = line[0].lower()
        line[2] = line[2].lower()
        f[line[0]] = f[line[2]] + 1
    
    write(str(max(f.values())))

if __name__ == "__main__":
    main()
