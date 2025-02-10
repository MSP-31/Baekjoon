# https://www.acmicpc.net/problem/2747

result = [0] * 46

num = int(input())

for i in range(num+1):
    if i <= 1:
        result[i] = i
    else:
        result[i] = result[i-1] + result[i-2]

print(result[num])