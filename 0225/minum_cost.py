import sys
sys.stdin = open('prac.txt','r')


def DFS(y, sum):
    global result

    if y == N:
        if result > sum:
            result = sum
        return

    if result < sum:
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            DFS(y+1, sum + Data[y][x])
            visited[x] = False

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = 987654321

    DFS(0, 0)
    print('#%d %d'%(tc, result))


# def minimum_cost(a, sum):
#     if a == n:
#         if result > sum:
#             result = sum
#         return
#
#     for i in range(n):
#         if test[i] == False:
#             test[i] = True
#             minimum_cost(a + 1, sum + case[a][i])
#             test[i] = False
#
#
# T = int(input())
#
# for t in range(T):
#     n = int(input())
#     case = [list(map(int, input().split())) for _ in range(n)]
#     test = [False] * n
#     result = 22276
#     minimum_cost(0, 0)
#     print(f'#{t + 1} {result}')