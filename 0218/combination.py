import sys
sys.stdin = open('prac.txt','r')

from functools import reduce
import operator

def com(n,r):
    result=0
    if n-r ==1:
        return n
    else:
        result+=reduce(operator.mul,range(1,n+1))
        result//=reduce(operator.mul,range(1,r+1))
        result//=reduce(operator.mul,range(1,n-r+1))
    return result % 1234567891



# def com(n, r):
#     tmp = 1
#     result=0
#     if n - r == 1:
#         return n
#     else:
#         for i in range(1, n + 1):
#             tmp *= i
#         result+=tmp
#         tmp = 1
#         for j in range(1, r + 1):
#             tmp *= j
#         result //= tmp
#         tmp = 1
#         for k in range(1, (n - r) + 1):
#             tmp *= k
#         result //= tmp
#     return result
#
# T = int(input())
#
# for t in range(T):
#     n, r = map(int, input().split())
#     print(f'#{t + 1} {com(n, r) % 1234567891}')

# def fac(n):
#     ans = 1
#     if n == 0:
#         return 1
#     else:
#         for i in range(1, n + 1):
#             ans *= i
#         return ans
#
# def com(n,r):
#     return fac(n) // fac(r) // fac(n-r)

T = int(input())

for t in range(T):
    n, r = map(int, input().split())
    print(f'#{t + 1} {com(n, r)}')
