# with open('test.txt', 'r') as file:
#     line=file.readlines()
#     total_score=0
#     for i in line:
#         total_score+=int(i)
#     result=total_score / len(line)
# with open('result.txt','w') as file:
#     file.write(f'{"총점 = "}{total_score}\n')
#     file.write(f'{"평균 = "}{result}')

import csv

filename='score.csv'
f=open(filename,'w',newline='')
wt=csv.writer(f)

wt.writerow(['이름','국어','수학','영어'])
wt.writerow(['홍길동',91,79,56])
wt.writerow(['성춘향',80,92,62])
wt.writerow(['김철수',73,66,81])
wt.writerow(['이순신',100,85,43])
wt.writerow(['J.K.Rowling',17,53,100])

f.close()

f2=open(filname,'r')
rd=csv.reader(f2)

for line in rd:
    print(line)

f.close()

