import sys
sys.stdin = open('prac.txt','r')

T = int(input())

for t in range(T):
    n = int(input())
    stop = [0] * 5000
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            stop[j] += 1

    p = int(input())
    result = []
    for i in range(p):
        result.append(int(input()))
    print(f'#{t+1}', end=' ')
    for i in result:
        print(stop[i], end=' ')
    print()