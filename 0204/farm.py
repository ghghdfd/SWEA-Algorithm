import sys
sys.stdin = open('prac.txt','r')

T = int(input())
for t in range(T):
    N = int(input())
    farm=[list(map(int,input().split())) for _ in range(N)]
    result = 0
    line=0
    start = (N-1)//2
    width = 1

    while width <= N:
        for i in range(width):
            result += farm[line][start+i]
        line += 1
        start -= 1
        width += 2

    start = 1
    width = N-2
    while width >= 1:
        for i in range(width):
            result += farm[line][start+i]
        line += 1
        start += 1
        width -= 2

    print(f'{t+1} {result}')