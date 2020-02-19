import sys
sys.stdin = open('prac.txt','r')

a = int(input())


for i in range(a):
    n, k = map(int,input().split())
    count=0
    puzzle=[list(map(int,input().split())) for i in range(n)]

    p1=[[str(puzzle[i][j]) for j in range(n)] for i in range(n)]
    p2=[[str(puzzle[j][i]) for j in range(n)] for i in range(n)]

    for j in range(n):
        if ''.join(p1[j]).split('0').count('1'*k) >=1:
            count+=''.join(p1[j]).split('0').count('1'*k)

        if ''.join(p2[j]).split('0').count('1'*k) >=1:
            count+=''.join(p2[j]).split('0').count('1'*k)

    print(f'#{i+1} {count}')
