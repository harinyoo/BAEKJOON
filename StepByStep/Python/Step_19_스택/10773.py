import sys

K = int(input())
stack = []
for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
