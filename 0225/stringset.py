import sys
sys.stdin = open('prac.txt','r')

#####처음 생각한 방법 : 시간 초과#####
# T = int(input())
#
# for t in range(T):
#     n, m = map(int, input().split())
#     case = [list(map(str, input().split())) for _ in range(2)]
#     case_2 = case[0] + case[1]
#     case_3 = []
#     for i in set(case_2):
#         case_3.append(i)
#
#     tmp = [0] * len(case_3)
#     count = 0
#     for i in range(len(case_3)):
#         if case_2.count(case_3[i]) >= 2:
#             tmp[i] += 1
#     for i in tmp:
#         if i == 1:
#             count += 1
#     print(f'#{t + 1} {count}')


#######리스트로 풀기 : 시간초과#######
# T=int(input())
#
# for t in range(T):
#     n,m=map(int,input().split())
#     case=[list(map(str,input().split())) for _ in range(2)]
#     case_1=case[0]
#     case_2=case[1]
#     case_3=[i for i in case_1 if i in case_2]
#     print(f'#{t+1} {len(case_3)}')


######정답코드: 세트로 만든 후 교집합 갯수 출력하기######

T=int(input())

for t in range(T):
    n,m=map(int,input().split())
    case=[set(map(str,input().split())) for _ in range(2)]
    case1=case[0]
    case2=case[1]
    count=len(case1 & case2)
    print(f'#{t+1} {count}')