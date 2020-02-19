from itertools import combinations
import sys
sys.stdin = open('prac.txt','r')

t = int(input())
for i in range(t):
    case = list(map(int, input().split()))
    case_2=list(combinations(case,3))
    result=list(set([sum(i) for i in case_2]))
    result=sorted(result,reverse=True)
    print(f'#{i + 1} {result[4]}')