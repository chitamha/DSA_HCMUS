import sys

write = sys.stdout.write

def main():
    n, m = map(int, input().split())
    table = [0] * m
    BASE = 53

    for _ in range(n):
        s = input()

        hash_value = 0
        for char in s:
            hash_value = (hash_value * BASE + ord(char)) % m
        
        if table[hash_value] == 0:
            table[hash_value] = 1
            write("0 0\n")
        else:
            flag = False
            for jump_count in range(1, 6):
                if table[(hash_value + jump_count) % m] == 0:
                    table[(hash_value + jump_count) % m] = 1
                    write(f"{jump_count} 0\n")
                    flag = True
                    break
            
            if not flag:
                write(f"5 {table[(hash_value + 5) % m]}\n")
                table[(hash_value + 5) % m] += 1

if __name__ == "__main__":
    main()