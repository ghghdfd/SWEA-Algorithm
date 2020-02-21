import sys
sys.stdin = open('prac.txt','r')

T = int(input())

for t in range(T):
    a = int(input())
    words = input().replace('!', '.').replace('?', '.').split('.')
    words.pop()
    print(f'#{t + 1}', end=' ')
    for i in range(a):
        words[i] = words[i].split()
        count = 0
        for j in range(len(words[i])):
            if words[i][j].isalpha():

                if words[i][j][0].isupper() and words[i][j][1:].islower():
                    count += 1

                if len(words[i][j]) == 1 and words[i][j][0].isupper():
                    count += 1

        print(count, end=' ')
    print('')

