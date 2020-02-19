import sys
sys.stdin=open('prac.txt','r')

t=int(input())
for i in range(t):
    v,e=map(int,input().split())
    g=[[0]*v for j in range(v)]
    print(g)


def dfs(i,total):
    global nums, many
    global count,result
    total +=nums[i]

