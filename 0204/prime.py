
case=set(i for i in range(3,1000001,2))
for i in range(3,1000001,2):
    if i in case:
        case-=set(i for i in range(i*2,1000001,i))
        print(case)
for i in len(case):
    print(case[i])

#
# case=set(i for i in range(3,1000001,2))
# case_2=[]
# for i in range(3,1000001,2):
#     if i in case:
#         for j in range(i*2,1000001,i):
#             case_2.append(j)
#
# case-=set(case_2)
# for i in case:
#     print(i)



case=[True]*1000000
n=int(1000000**0.5)
for i in range(2,n+1):
    if case[i] == True:
        for j in range(i*2,1000000,i):
            case[j]=False
result=[i for i in range(2,1000000) if case[i]==True]
for i in result:
    print(i,end=' ')

