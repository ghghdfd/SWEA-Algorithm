import sys
sys.stdin = open('prac.txt','r')


for i in range(1, 11):
    n = int(input())
    count = 0
    case = list(map(int, input().split()))
    for j in range(2, n - 2):
        if case[j] == max(case[j - 2:j + 3]):
            case_2 = case[j - 2:j + 3]
            case_2.sort()
            count += case_2[-1] - case_2[-2]
    print(f'#{i} {count}')
