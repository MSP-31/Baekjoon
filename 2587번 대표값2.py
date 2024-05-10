# https://www.acmicpc.net/problem/2587

num = []

for i in range(5):
    num.append(int(input()))

# 정렬
num.sort()

print(int(sum(num)/len(num)))
print(num[2])