# https://www.acmicpc.net/problem/1546

n = int(input())
m = list(map(int,input().split()))

max_m = max(m)
sum = 0

for i in range(n):
    sum += m[i]/max_m * 100
print(sum/n)