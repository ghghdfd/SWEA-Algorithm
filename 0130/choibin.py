import sys
sys.stdin = open('prac.txt','r')

n=int(input())

for i in range(n):
    num=int(input())
    case=list(map(int,input().split()))
    counts={j:case.count(j) for j in set(case)}
    for x in counts.keys():
        if max(counts.values()) ==  counts[x]:
            print(f'#{i+1} {x}')
        
