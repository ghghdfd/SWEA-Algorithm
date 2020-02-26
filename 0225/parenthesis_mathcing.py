# import sys
# sys.stdin = open('prac.txt','r')

for t in range(1):
    length=int(input())
    case=input()
    test=['(',')','[',']','<','>','{','}']
    count_result=[case.count(i) for i in test]
    if count_result[0] == count_result[1] and count_result[2] == count_result[3] \
            and count_result[4] ==count_result[5] and count_result[6] == count_result[7]:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')