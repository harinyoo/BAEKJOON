import sys

N = int(input())
triangle = []
for n in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[N-1]))
