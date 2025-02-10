# https://www.acmicpc.net/problem/8393

n = int(input())
sum = 0
"""
단순 로직
for i in range(1,n+1):
    sum += i
print(sum)
"""
# 가우스의 합
sum = n*(n+1)/2

print(int(sum))