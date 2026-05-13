import sys

write = sys.stdout.write

def main():
    n = int(input())
    hash_table = {}
    for _ in range(n):
        name = input()
        if name in hash_table:
            hash_table[name] += 1
            write(f"{name}{hash_table[name]}\n")
        else:
            hash_table[name] = 0
            write("OK\n")

if __name__ == "__main__":
    main()
