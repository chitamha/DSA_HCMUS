import sys
def be_Untangled_Wires(line):
    if len(line) % 2 == 1:
        return False
    
    stack = []
    for i in range(len(line)):
        if not stack:
            stack.append(line[i])
        else:
            if stack[-1] == line[i]:
                stack.pop()
            else:
                stack.append(line[i])
                
    # print(stack)
    return len(stack) == 0

line = sys.stdin.readline().strip()

if be_Untangled_Wires(line):
    print("Yes")
else:
    print("No")