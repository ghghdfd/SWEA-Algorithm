import sys
sys.stdin = open('prac.txt','r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    # print(G)
    for i in range(N):
        temp = list(map(int, input().split()))
        G[i] = temp

    print(G)