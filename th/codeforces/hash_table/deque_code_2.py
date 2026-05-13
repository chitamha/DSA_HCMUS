import sys

write = sys.stdout.write

def main():
    q = int(input())
    deque = [0] * 200001
    head = tail = 100000
    # tail là vị trí sau tail của deque (fake), head là vị trí head của deque (real)
    for _ in range(q):
        command = input().split()
        if command[0] == '1':
            deque[tail] = int(command[1])
            tail += 1
        elif command[0] == '2':
            deque[head - 1] = int(command[1])
            head -= 1
        elif command[0] == '3':
            write(str(deque[tail - 1]) + '\n')
            tail -= 1
        elif command[0] == '4':
            write(str(deque[head]) + '\n')
            head += 1
        else:
            write(str(deque[head + int(command[1])]) + '\n')

if __name__ == "__main__":
    main()
