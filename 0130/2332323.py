T = int(input())

for i in range(T):
    case = input()
    for j in range(1, 11):
        if case[0:j] == case[j:2 * j] :
            if j <= 5:
                print(f'#{i + 1} {j}')
                break
            else:
                print(f'#{i + 1} {j}')
