import sys
sys.stdin = open('prac.txt','r')

n=int(input())

for i in range(n):
    case=input()
    for j in range(1,len(list(case))):
        if case[:j] == case[j:j*2]:
            print(f'#{i+1} {j}')
            break