import sys
sys.stdin = open('prac.txt','r')

T = int(input())
for t in range(T):
    k,n,m= map(int,input().split())
    station = list(map(int, input().split()))
    station_list = [0] * (n+1)

    for i in range(len(station)):
        station_list[station[i]] += 1

    start = 0
    end = k
    count = 0

    while True:
        zero = 0
        for i in range(start+1, end+1):
            if station_list[i] == 1:
                start = i
            else:
                zero += 1

        if zero == k:
            count = 0
            break

        count += 1
        end = start + k

        if end >= n:
            break

    print(f'{t+1} {count}')