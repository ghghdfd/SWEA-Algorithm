import sys
sys.stdin = open('prac.txt','r')

a = int(input())

for i in range(a):
    b = int(input())
    print(f'#{i+1}')
    result = ''

    for j in range(b):
        case = input().split()

        for k in range(int(case[1])):

            result+=case[0]
            if len(result) == 10:
                print(result)
                result=''
    print(result)
