def fibonacci(num):
    if num == 1:
        return a

    tmp = fibonacci(num // 2)
    b = [[0, 0], [0, 0]]
    c = [[0, 0], [0, 0]]
    if num % 2:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    b[i][j] += tmp[i][k] * tmp[k][j]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] += b[i][k] * a[k][j]
                c[i][j] %= 1000000007
        return c
    else:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    b[i][j] += tmp[i][k] * tmp[k][j]
                b[i][j] %= 1000000007
        return b


n = int(input())
a = [[1, 1], [1, 0]]
print(fibonacci(n)[0][1])


#---------------------------------------------------------------------
# import sys
# input=sys.stdin.readline
# p=1000000007
# #제곱을 구하는 분할정복
# def power(adj,n):
#     if n==1:
#         return adj
#     elif n%2:
#         return multi(power(adj,n-1),adj)
#     else:
#         return power(multi(adj,adj),n//2)
# #행렬의 곱셈
# def multi(a,b):
#     temp=[[0]*len(b[0]) for _ in range(2)]
#     for i in range(2):
#         for j in range(len(b[0])):
#             sum=0
#             for k in range(2):
#                 sum+=a[i][k]*b[k][j]
#             temp[i][j]=sum%p
#     return temp
# #초기 행렬
# adj=[[1,1],[1,0]]
# #피보나치 초기값
# start=[[1],[1]]
# n=int(input())
# if n<3:
#     print(1)
# else:
#     print(multi(power(adj,n-2),start)[0][0])



