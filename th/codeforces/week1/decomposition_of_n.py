import sys

n = int(sys.stdin.readline())
current_partition = []

def findDecompositions(target_sum,  max_value):
    if target_sum == 0:
        print(" + ".join(map(str, current_partition)))
        return
    
    for number in range(min(target_sum, max_value), 0, -1):
        current_partition.append(number)
        findDecompositions(target_sum - number, number)
        current_partition.pop()

findDecompositions(n, n)