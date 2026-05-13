import sys

def catch_Overflow():
    n = int(sys.stdin.readline())

    number = 0
    stack = [1]
    # stack sẽ chứa giá trị nhân dồn hiện tại
    LIMIT = (1 << 32) - 1;

    for i in range(n):
        line = sys.stdin.readline().split()
        command = line[0]

        if command == "for":
            increment = int(line[1])
            stack.append(min(LIMIT + 1, stack[-1] * increment))

        elif command == "add":
            number += stack[-1]
            if number > LIMIT:
                print("OVERFLOW!!!")
                return

        else:
            stack.pop()
    
    print(number)

catch_Overflow()