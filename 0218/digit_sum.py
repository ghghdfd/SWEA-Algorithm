import sys
sys.stdin = open('prac.txt','r')

def digit_sum(n):
    temp=0
    for i in n:
        temp+=int(i)
    if len(str(temp)) ==1:
        return temp
    else:
        digit_sum(list(str(temp)))

T=int(input())

for i in range(T):
    case=list(input())
    digit_sum(case)
for i in range(T):
    print(f'#{i+1} {temp}')