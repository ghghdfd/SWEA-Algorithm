import sys
sys.stdin = open('prac.txt','r')

from itertools import combinations

T=int(input())
A=[1,2,3,4,5,6,7,8,9,10,11,12]

for t in range(T):
    n,k= map(int,input().split())
    count=0
    for i in combinations(A,n):
        if sum(i) == k:
            count+=1
    print(f'#{t+1} {count}')



#######경환이형 솔루션 ######
# def combi(arr, count, last):
#     global count, many, target, A, answer
#     if count == many:
#         if sum(arr) == target:
#             answer += 1
#             return
#     else:
#         for i in range(last, len(A)):
#             ar = arr[:]
#             ar.append(A[i])
#             combi(ar, count + 1, i + 1)


#
# def combi(arr, depth, last):
#     global count
#     if depth == M:
#         count += 1
#         print('c', count, ':', arr)
#     else:
#         for i in range(last, N+1):
#             ar = arr[:]
#             ar.append(i)
#             combi(ar, depth + 1, i + 1)
#
#
# N, M = map(int, input().split())
# count = 0
# combi([], 0, 0)

