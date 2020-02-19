# import sys
# sys.stdin = open('prac.txt','r')

# def seq(a, b):
#     global count
#     if a >= t:
#         return
#     result = b + case[a]
#     if result == k:
#         count += 1
#     seq(a + 1, b)
#     seq(a + 1, result)
#
#
# t = int(input())
#
# for i in range(t):
#     n, k = map(int, input().split())
#     case = list(map(int, input().split()))
#     count = 0
#     summ = 0
#     for j in range(t):
#         if summ + case[j] == k:
#             count += 1
#     seq(0, 0)
#     print(f'#{i + 1} {count}')


def sequence(index, startsum):
    global count
    if index >= n:
        return
    result = startsum + case[index]
    if result == k:
        count += 1
    sequence(index+1,startsum)
    sequence(index+1,result)

a = int(input())
for i in range(a):
    n, k = map(int, input().split())
    case = list(map(int, input().split()))
    count = 0
    startsum = 0
    for j in range(len(case)):
        if startsum + case[j] == k:
            count += 1
        sequence(0, 0)
    print(f'#{i+1}{count}')