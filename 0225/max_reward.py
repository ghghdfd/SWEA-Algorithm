import sys
sys.stdin = open('prac.txt','r')


T=int(input())

for t in range(T):
    case,n= map(str,input().split())
    case=list(case)
    temp=[]
    print(f'#{t+1}',end=' ')
    for i in range(int(n)):
        temp.append(case.pop(case.index(max(case))))
    for i in range(len(case)):
        temp.append(case.pop(case.index(max(case))))
    for i in range(len(temp)):
        print(int(temp[i]),end='')
    print()