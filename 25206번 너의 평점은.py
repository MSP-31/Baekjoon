# https://www.acmicpc.net/problem/25206

score = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0,}

sum = 0
grades_sum = 0

for i in range(20):
    a = list(input().split())
    if 'P' != a[2]:
        sum += float(a[1]) * score[a[2]]
        grades_sum += float(a[1])
    else:
        continue
print(round(sum/grades_sum,6))