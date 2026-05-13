import sys

def minimalString(s):
    count = [0] * 26
    t = []
    u = []

    for char in s:
        count[ord(char) - ord('a')] += 1

    min_c = 0
    for char in s:
        t.append(char)
        count[ord(char) - ord('a')] -= 1
        while (min_c < 26 and count[min_c] == 0):
            min_c += 1
        while t and min_c >= ord(t[-1]) - ord('a'):
            u.append(t[-1])
            t.pop()
    
    print("".join(u))

s = sys.stdin.readline().strip()
minimalString(s)
        

    

