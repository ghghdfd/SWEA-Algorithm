import sys
sys.stdin = open('prac.txt','r')

def binary(case,key):
    start=0
    end=len(case)
    count=0
    while True:
        mid= (start+end)//2
        if key < case[mid]:
            end = mid
            count+=1
        elif key == case[mid]:
            count+=1
            return count
            break
        elif key > case[mid]:
            start= mid
            count+=1


T = int(input())

for t in range(T):
    p, a, b = map(int, input().split())
    case = [i for i in range(1,p)]
    if binary(case,a) > binary(case,b):
        print(f'#{t+1} B')
    elif binary(case,a) < binary(case,b):
        print(f'#{t+1} A')
    elif binary(case,a) == binary(case,b):
        print(f'#{t+1} 0')