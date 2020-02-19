import sys
sys.stdin = open('prac.txt','r')

for i in range(10):
    n=int(input())
    case = list(map(int, input().split()))
    for j in range(n):
        if max(case) - min(case) >=1:
            case.sort()
            case[0]+=1
            case[-1]-=1
        else:
            break
    result= max(case) - min(case)
    print(f'#{i+1} {result}')







