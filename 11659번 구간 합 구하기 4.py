# https://www.acmicpc.net/problem/11659
# input() 대신에 sys.stdin.readline() 사용해야함
# input은 느림;;

import sys

n,m = map(int,sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))

# 누적합
value = [0] * (n + 1)
for i in range(n):
    value[i + 1] = value[i] + x[i]

result = []
for _ in range(m):
    i , j = map(int,input().split())
    
    if i == 1:
        result.append(value[j])
    else:
        result.append(value[j]-value[i-1])

for res in result:
    print(res)