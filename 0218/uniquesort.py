import sys
sys.stdin = open('prac.txt','r')

T=int(input())
for t in range(T):
    n = int(input())
    case = list(map(int,input().split( )))
    result = []
    print(f'#{t+1}',end=' ')
    for i in range(5):
        result.append(case.pop(case.index(max(case))))
        result.append(case.pop(case.index(min(case))))
    for i in range(len(result)):
        print(f'{result[i]}',end=' ')
    print()